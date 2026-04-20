from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)  # days before repeating

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Completion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('habit', 'date')  # prevent duplicate completions

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
    
class Pet(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE, related_name='pet')
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return f"Pet for {self.habit.name} ({self.habit.user.username})"