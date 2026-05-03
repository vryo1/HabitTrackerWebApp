# Sprint 3 Report (4/4/26 - 5/2/26)

## What's New (User Facing)
* Display a heatmap alongside each habit, displaying completed and missed days.
* Feature 2 or Bug Fix 2
* Feature n or Bug Fix n

## Work Summary (Developer Facing)
To display the heatmap, each habit now includes the date created in the database.
In the backend, the completions are passed to the frontend dashboard template to show completed and missed days on the heatmap.
And in the frontend, JavaScript builds the grid starting from the habit start date.

## Unfinished Work
Overall there is no unfished work but we will begin implementing a heatmap that tracks every habit not just per habit so the users can see a better overall understanding. 

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/21
* URL of issue 2
  
GitHub
* Each issue should be assigned story points using a label
* Story points contribution of each team member should be indicated in a comment

## Incomplete Issues/User Stories
N/A

## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* [views.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/views.py)
* [dashboard.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/dashboard.html)
* [models.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/models.py)

## Retrospective Summary
Here's what went well:
* The project is where we wanted it to be by the end of the 3rd and final sprint.
* Item 2
* Item x
Here's what we'd like to improve:
* Improve code consistency and maintainability by moving HTML styles into CSS classes.
* Item 2
* Item x
Here are changes we plan to implement in the next sprint:
* a heatmap that tracks every habit not just per habit.
* Item 2
* Item x
