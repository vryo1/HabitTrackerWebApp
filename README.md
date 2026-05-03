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
As of now, TheDailyNudge-HabitTrackerWebApp is a Django web app backed by PostgreSQL hosted on Supabase.
### Prerequisites
- Git
- Python 3.12+ and pip
- A virtual environment tool (recommended: built-in venv)
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
2. **Create and activate virtual environment**
```
python -m venv venv
.\venv\Scripts\Activate.ps1  (Windows)
source venv/bin/activate     (Mac/Linux)
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Set up environment variables**
```
cp .env.example .env
```
Edit `.env` and fill in:
```
SECRET_KEY=your-own-long-random-string
DATABASE_URL=ask-a-team-member-for-the-supabase-url
```
5. **Apply datbase migrations**
```
cd client
python manage.py migrate
```
6. **Run the development server**
```
python manage.py runserver
```
The app will be available at `http://127.0.0.1:8000/`

7. **Run Unit tests**
```
python manage.py test Backend --keepdb
```
All 24 tests should pass. The `--keepdb` flag preserves the test database between runs to avoid cleanup conflicts with Supabase.

## Functionality
**Login Page** - Existing users can log in with their username and password

**Create Account Page** - New users can register by choosing a username and password.

**Dashboard** - The main page after logging in. Each habit displays its name, current streak, pet companion that evolves based on streak length, a progress bar toward the next pet stage, and a heatmap showing completed and missed days. Notification banners remind you to complete habits that are due today.

**Manage Habits Page** - Use this page to add new habits to the tracker. Press "Add Habit" then fill out the habit details and press "Add" to save it. The habit will then appear on the dashboard.

## Testing
Unit tests are located in `client/Backend/tests.py` and cover streak calculation, pet stage logic, due date calculation, habit CRUD operations, and pet naming. To run:
```
cd client
python manage.py test Backend --keepdb
```
Expected output: `Ran 24 tests OK
`
## Known Problems
The app is hosted on Supabase's free tier, which pauses the database after periods of inactivity. If the app appears unresponsive, visit the Supabase dashboard to resume the project.

## Additional Documentation
