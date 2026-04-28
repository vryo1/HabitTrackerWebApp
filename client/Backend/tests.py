from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from Backend.models import Habit, Completion, Pet
from Backend.views import calculate_streak, calculate_pet_stage, calculate_due
# Create your tests here.

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from Backend.models import Habit, Completion, Pet
from Backend.views import calculate_streak, calculate_pet_stage, calculate_due


class CalculateStreakTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.habit = Habit.objects.create(user=self.user, name='Test Habit', frequency=1)

    def test_no_completions_returns_zero(self):
        self.assertEqual(calculate_streak(self.habit), 0)

    def test_single_completion_today(self):
        Completion.objects.create(habit=self.habit, date=date.today())
        self.assertEqual(calculate_streak(self.habit), 1)

    def test_consecutive_daily_streak(self):
        today = date.today()
        for i in range(5):
            Completion.objects.create(habit=self.habit, date=today - timedelta(days=i))
        self.assertEqual(calculate_streak(self.habit), 5)

    def test_streak_breaks_after_gap(self):
        today = date.today()
        Completion.objects.create(habit=self.habit, date=today)
        Completion.objects.create(habit=self.habit, date=today - timedelta(days=2))
        self.assertEqual(calculate_streak(self.habit), 1)

    def test_frequency_two_allows_gap(self):
        self.habit.frequency = 2
        self.habit.save()
        today = date.today()
        Completion.objects.create(habit=self.habit, date=today)
        Completion.objects.create(habit=self.habit, date=today - timedelta(days=2))
        self.assertGreater(calculate_streak(self.habit), 1)

    def test_streak_preserved_without_todays_completion(self):
        yesterday = date.today() - timedelta(days=1)
        Completion.objects.create(habit=self.habit, date=yesterday)
        self.assertEqual(calculate_streak(self.habit), 1)


class CalculatePetStageTests(TestCase):
    def test_egg_stage(self):
        self.assertEqual(calculate_pet_stage(0), 1)
        self.assertEqual(calculate_pet_stage(2), 1)

    def test_hatchling_stage(self):
        self.assertEqual(calculate_pet_stage(3), 2)
        self.assertEqual(calculate_pet_stage(6), 2)

    def test_companion_stage(self):
        self.assertEqual(calculate_pet_stage(7), 3)
        self.assertEqual(calculate_pet_stage(13), 3)

    def test_guardian_stage(self):
        self.assertEqual(calculate_pet_stage(14), 4)
        self.assertEqual(calculate_pet_stage(29), 4)

    def test_legend_stage(self):
        self.assertEqual(calculate_pet_stage(30), 5)
        self.assertEqual(calculate_pet_stage(100), 5)


class CalculateDueTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='pass')
        self.habit = Habit.objects.create(user=self.user, name='Due Habit', frequency=3)

    def test_no_completions_returns_zero(self):
        self.assertEqual(calculate_due(self.habit), 0)

    def test_completed_today_returns_frequency(self):
        Completion.objects.create(habit=self.habit, date=date.today())
        self.assertEqual(calculate_due(self.habit), 3)

    def test_completed_yesterday_returns_two(self):
        Completion.objects.create(habit=self.habit, date=date.today() - timedelta(days=1))
        self.assertEqual(calculate_due(self.habit), 2)

    def test_overdue_returns_zero(self):
        Completion.objects.create(habit=self.habit, date=date.today() - timedelta(days=5))
        self.assertEqual(calculate_due(self.habit), 0)


class HabitViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewuser', password='pass')
        self.client.login(username='viewuser', password='pass')
        self.habit = Habit.objects.create(user=self.user, name='View Habit', frequency=1)

    def test_dashboard_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_complete_habit_creates_completion(self):
        response = self.client.post(reverse('complete_habit', args=[self.habit.id]))
        self.assertEqual(Completion.objects.filter(habit=self.habit, date=date.today()).count(), 1)

    def test_complete_habit_no_duplicate(self):
        self.client.post(reverse('complete_habit', args=[self.habit.id]))
        self.client.post(reverse('complete_habit', args=[self.habit.id]))
        self.assertEqual(Completion.objects.filter(habit=self.habit, date=date.today()).count(), 1)

    def test_add_habit(self):
        response = self.client.post(reverse('managehabits'), {'name': 'New Habit', 'frequency': 1})
        self.assertTrue(Habit.objects.filter(user=self.user, name='New Habit').exists())

    def test_delete_habit(self):
        response = self.client.post(reverse('delete_habit', args=[self.habit.id]))
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())

    def test_dashboard_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/login/?next=/dashboard/')


class PetTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='petuser', password='pass')
        self.habit = Habit.objects.create(user=self.user, name='Pet Habit', frequency=1)

    def test_pet_created_with_habit_on_dashboard(self):
        self.client.login(username='petuser', password='pass')
        self.client.get(reverse('dashboard'))
        self.assertTrue(Pet.objects.filter(habit=self.habit).exists())

    def test_name_pet(self):
        Pet.objects.create(habit=self.habit)
        self.client.login(username='petuser', password='pass')
        self.client.post(reverse('name_pet', args=[self.habit.id]), {'pet_name': 'Buddy'})
        pet = Pet.objects.get(habit=self.habit)
        self.assertEqual(pet.name, 'Buddy')