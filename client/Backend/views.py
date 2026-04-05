from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta
from Backend.models import Habit, Completion
from django.contrib import messages


# Helper function to calculate the current streak for a habit
def calculate_streak(habit):
    today = date.today()
    streak = 0
    current_day = today

    while True:
        exists = Completion.objects.filter(habit=habit, date=current_day).exists()
        if exists:
            streak += 1
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

@login_required(login_url='login')
def dashboard(request):
    habits = request.user.habit_set.all()
    habit_data = []
    for habit in habits:
        habit_data.append({
            'habit': habit,
            'streak': calculate_streak(habit),
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