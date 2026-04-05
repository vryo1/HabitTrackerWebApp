# Sprint 2 Report (3/1/26 - 4/4/26)

## What's New (User Facing)
* Feature 1: Display habits on the manage habits page
* Feature 2: Allow users to edit and delete existing habits
* Feature 3: Polished manage habits page
* Feature 4: Hosted PostgreSQL database remotely on Supabase
* Feature 5: Habit completion tracking with streak updates
* Feature 6: Registered Habit and Completion models in Django admin panel
* Feature 7: Secured credentials using environment variables
* Feature 8: Updated signup UI
  
## Work Summary (Developer Facing)
On the backend, habit completion tracking was implemented allowing users to mark habits as done for the day, with duplicate prevention handled through Django's get_or_create method. 
The database was migrated from local PostgreSQL to a remotely hosted Supabase instance, eliminating the local set up requirement for all team members. 
Habit and Completion models were also registered in the Django admin panel for easier data management.
Sign up UI was also updated to match Login UI, including font, color and overall theme.

## Unfinished Work
* All sprint 2 issues were completed.
  
## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/13
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/16
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/17
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/14
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/15
  
## Incomplete Issues/User Stories
* No incomplete issues for this sprint. All issues opened during Sprint 2 were completed and closed before the sprint deadline.

## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* [views.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/views.py )
* [managehabits.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/managehabits.html)
* [urls.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/TheDailyNudge/urls.py)
* [admin.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/admin.py)
* [dashboard.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/dashboard.html)
* [signup.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/signup.html)

## Retrospective Summary
Here's what went well:
* We coordinated backend auth logic and frontend template updates early, which made testing and integration faster.
* Successfully migrated database to Supabase eliminating local setup requirement.
* Habit completion tracking implemented.
* Django admin panel now shows Habit and Completion models for easier debugging.

Here's what we'd like to improve:
* More timely and frequent commits throughout the sprint.
* Security upgrades
* Start on issues earlier

Here are changes we plan to implement in the next sprint:
* Weekly commits
* Heatmap visualization for habit completion history 
* Start testing features
