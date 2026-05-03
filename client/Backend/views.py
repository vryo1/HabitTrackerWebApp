from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta
from Backend.models import Habit, Completion, Pet
from django.contrib import messages


def calculate_streak(habit):
    today = date.today()
    frequency = habit.frequency
    
    # If not yet completed today, start checking from yesterday
    completed_today = Completion.objects.filter(habit=habit, date=today).exists()
    current_day = today if completed_today else today - timedelta(days=1)
    
    streak = 0

    while True:
        exists = Completion.objects.filter(habit=habit, date=current_day).exists()

        if exists:
            streak += 1
            current_day -= timedelta(days=1)
        else:
            gap_end = current_day - timedelta(days=frequency - 1)
            any_in_gap = Completion.objects.filter(
                habit=habit,
                date__gte=gap_end,
                date__lte=current_day
            ).exists()

            if any_in_gap:
                current_day -= timedelta(days=1)
            else:
                break

    return streak

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def calculate_due(habit):
    today = date.today()
    frequency = habit.frequency

    last_completion = Completion.objects.filter(habit=habit).order_by('-date').first()

    if not last_completion:
        return 0 

    days_since = (today - last_completion.date).days
    days_until_due = frequency - days_since

    return days_until_due

@login_required(login_url='login')
def dashboard(request):
    habits = request.user.habit_set.all()
    habit_data = []
    today = date.today()
    for habit in habits:
        streak = calculate_streak(habit)
        pet, created = Pet.objects.get_or_create(habit=habit)
        stage = calculate_pet_stage(streak)

        if stage == 1:
            progress = (streak / 3) * 100
        elif stage == 2:
            progress = ((streak - 3) / 4) * 100
        elif stage == 3:
            progress = ((streak - 7) / 7) * 100
        elif stage == 4:
            progress = ((streak - 14) / 16) * 100
        else:
            progress = 100
        completed_today = Completion.objects.filter(habit=habit, date=today).exists()
        completions = list(Completion.objects.filter(habit=habit).values_list('date', flat=True))
        completion_set = [d.isoformat() for d in completions]
        days_until_due = calculate_due(habit)
        habit_data.append({
            'habit': habit,
            'streak': streak,
            'pet': pet,
            'pet_stage': stage,
            'pet_image': f'images/pets/pet_stage{stage}.png',
            'pet_progress': min(round(progress), 100),
            'needs_name': streak >= 3 and not pet.name,
            'completed_today': completed_today,
            'completion_dates': completion_set,
            'days_until_due': days_until_due,
        })
    return render(request, 'dashboard.html', {'habit_data': habit_data})

@login_required(login_url='login')
def manage_habits(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        frequency = request.POST.get('frequency')

        if not name:
            messages.error(request, "Habit name cannot be empty.")
            return redirect('managehabits')

        # Convert frequency to integer and handle invalid input
        try:
            frequency = int(frequency)
            if frequency < 1:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, "Frequency must be a positive integer.")
            return redirect('managehabits')

        # Create habit
        Habit.objects.create(
            user=request.user,
            name=name,
            frequency=frequency
            )
        messages.success(request, "Habit added successfully!")
        return redirect('managehabits')

    # GET request — show all habits
    habits = request.user.habit_set.all()
    return render(request, 'managehabits.html', {'habits': habits})

@login_required(login_url='login')
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        frequency = request.POST.get('frequency')

        if not name:
            messages.error(request, "Habit name cannot be empty.")
            return redirect('managehabits')

        try:
            frequency = int(frequency)
            if frequency < 1:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, "Frequency must be a positive integer.")
            return redirect('managehabits')

        habit.name = name
        habit.frequency = frequency
        habit.save()

        messages.success(request, "Habit updated successfully!")
        return redirect('managehabits')
    return redirect('managehabits')
    
@login_required(login_url='login')
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        habit.delete()
        messages.success(request, "Habit deleted successfully!")

    return redirect('managehabits')

@login_required(login_url='login')
def complete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id =habit_id, user=request.user)

    if request.method == 'POST':
        today = date.today()
        completion, created = Completion.objects.get_or_create(habit=habit, date=today) #prevent duplicates
        if created : 
            messages.success(request, f"{habit.name} marked as complete!")
        else:
            messages.info(request, f"{habit.name} already completed today.")
    
    return redirect('dashboard')

def calculate_pet_stage(streak):
    if streak <= 2:
        return 1  # egg
    elif streak <= 6:
        return 2  # hatchling
    elif streak <= 13:
        return 3  # companion
    elif streak <= 29:
        return 4  # guardian
    else:
        return 5  # legend

@login_required(login_url='login')
def name_pet(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name', '').strip()
        if pet_name:
            pet, _ = Pet.objects.get_or_create(habit=habit)
            pet.name = pet_name
            pet.save()
            messages.success(request, f"Your pet has been named {pet_name}!")
    return redirect('dashboard')