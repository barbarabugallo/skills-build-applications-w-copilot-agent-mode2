import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, LeaderboardEntry
from django.utils import timezone

# Clear existing data
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Workout.objects.all().delete()
LeaderboardEntry.objects.all().delete()

# Create Users
user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')
user3 = User.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Lee')

# Create Teams
team1 = Team.objects.create(name='Team Alpha', description='First team')
team2 = Team.objects.create(name='Team Beta', description='Second team')
team1.members.add(user1, user2)
team2.members.add(user3)

# Create Workouts
workout1 = Workout.objects.create(name='Morning Run', description='5km easy run', suggested_for='beginners', difficulty='easy')
workout2 = Workout.objects.create(name='HIIT', description='High intensity interval training', suggested_for='advanced', difficulty='hard')

# Create Activities
activity1 = Activity.objects.create(user=user1, activity_type='run', duration_minutes=30, calories_burned=250, date=timezone.now().date(), team=team1)
activity2 = Activity.objects.create(user=user2, activity_type='cycle', duration_minutes=45, calories_burned=400, date=timezone.now().date(), team=team1)
activity3 = Activity.objects.create(user=user3, activity_type='swim', duration_minutes=60, calories_burned=500, date=timezone.now().date(), team=team2)

# Create Leaderboard Entries
LeaderboardEntry.objects.create(user=user1, team=team1, total_points=120)
LeaderboardEntry.objects.create(user=user2, team=team1, total_points=100)
LeaderboardEntry.objects.create(user=user3, team=team2, total_points=150)

print('Test data populated successfully!')
