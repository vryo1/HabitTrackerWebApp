# HabitTrackerWebApp
# Project Name: 
The Daily Nudge 
## Project summary: 
The project will be a web app that can be used by users to create habits that repeat over a
specified frequency, as well as manage those habits and adjust them to suit their goals. The UI
will is intuitive to make tracking habits the main focus, while remaining easy to do other
tasks like creating new habits and managing existing ones.
### One-sentence description of the project
TheDailyNudge is an intuitive habit tracking web app that helps users create, customize, and manage recurring habits around their personal goals, so daily progress stays front and center and long term behavior change becomes consistency made simple.
### Additional information about the project
The main/home page will present multiple habits with a clear button to allow users to mark
whether they did the habit on that day. Along with the habit, it will display a heatmap, showing
which habits users might be struggling on and which habits they do a good job of completing. A
secondary menu will then allow users to create and customize new habits, as well as manage
and adjust the existing ones.
## Installation
As of now, TheDailyNudge-HabitTrackerWebApp is a Django web app backed by PostgreSQL.
### Prerequisites
- Git
- Python 3.12+ and pip
- A virtual environment tool (recommended: built-in venv)
- PostgreSQL running locally (default port 5432)
- A database/user matching current updated local config
### Add-ons 
- Django==6.0.2: Core web framework for routing, templates, models, and auth.
- psycopg2-binary==2.9.11: PostgreSQL adapter used by Django.
- django-environ==0.13.0: Reads environment variables for secure configuration.
- asgiref==3.11.1: ASGI support used by Django runtime.
- sqlparse==0.5.5: SQL parsing utility used by Django internals.
- tzdata==2025.3: Time zone database for consistent date/time handling.
### Installation Steps
1. **Clone the repository**
```
git clone https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp.git
cd HabitTrackerWebApp
```
2. **Install dependencies**
```
pip install -r requirements.txt
```
3. **Set up local database (PostgreSQL)**
Make sure PostgreSQL is running, then create your own database user and password (do not use shared hardcoded credentials).

```sql
CREATE USER your_db_user WITH PASSWORD 'your_strong_password';
CREATE DATABASE habittracker OWNER your_db_user;
```
4. **Apply datbase migrations**
```
cd client
python manage.py migrate
```
5. **Start the app**
```
python manage.py runserver
```
The app will be available at `http://127.0.0.1:8000/`

## Functionality
**Login Page** - Existing users can log in with their username and password

**Create Account Page** - New users can register by choosing a username and password.

**Dashboard** - This is the main page after logging in, where you can view all of your current habits. Each habit is displayed with its name and streak.

**Manage Habits Page** - Use this page to add new habits to the tracker. Press "Add Habit" then fill out the habit details and press "Add" to save it. The habit will then appear on the dashboard.

## Known Problems
**PostgreSQL must be running locally** - The app requires a local PostgreSQL instance to be running in order to connect to the database. If you see a database connection error on startup, make sure PostgreSQL is installed and running on your machine before launching the app.

## Additional Documentation
