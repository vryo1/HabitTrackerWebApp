# Sprint 3 Report (4/4/26 - 5/2/26)
https://youtu.be/_XRocVDm-gM
## What's New (User Facing)
* Heatmap visualization alongside each habit displaying completed and missed days.
* Pet evolution system: each habit has a pet that evolves through 5 stages based on streak length, with a progress bar and naming prompt
* In-app notification banners reminding users to complete habits that are due today
* Fixed streak calculation to correctly respect each habit's custom frequency setting
* Empty state prompt on the dashboard for new users
* Unit tests written and passing for all core backend logic

## Work Summary (Developer Facing)
The heatmap was added by storing each habit's creation date, passing completion records to the dashboard, and building the grid in JavaScript from the habit's start date. Missed days are highlighted in red.
The pet evolution system was implemented with a new Pet model linked to each habit, a `calculate_pet_stage` function, and dashboard updates including pet images, a progress bar, and a naming prompt at streak 3.
The streak calculation was fixed to respect habit frequency. Gaps up to the frequency length no longer break the streak, and extra completions still count toward building it faster.
Notification banners were added by computing a `completed_today` flag per habit in the dashboard view and rendering a dismissible banner for any habit due today but not yet completed.
24 automated unit tests were written using Django's built-in test framework covering streak calculation, pet stages, due dates, habit CRUD, and pet naming. All 24 pass

## Unfinished Work
* #27 Motivational quote/affirmation on habit completion — we ran out of time to implement this feature before the sprint deadline. It has been moved to future work.
* #28 Dashboard summary stats — we ran out of time to implement this feature before the sprint deadline. It has been moved to future work.
* #30 Track longest streak record per habit — we ran out of time to implement this feature before the sprint deadline. It has been moved to future work.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/21
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/22
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/23
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/24
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/25
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/26
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/29
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/31
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/19

## Incomplete Issues/User Stories
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/27 — we ran out of time to implement motivational quotes before the sprint deadline.
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/28 — we ran out of time to implement dashboard summary stats before the sprint deadline.
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/30 — we ran out of time to implement longest streak tracking before the sprint deadline.

## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* [views.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/views.py)
* [dashboard.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/dashboard.html)
* [models.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/models.py)
* [tests.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/tests.py)

## Retrospective Summary
Here's what went well:
* All core Sprint 3 features were completed and the app is fully functiona end to end.
* Unit tests were written and all 24 pass, giving the team confidence in backend logic.
* The pet evolution system added a unique engagement mechanic that differentiates the app from similar projects.

Here's what we'd like to improve:
* More consistent and frequent commits throughout the sprint rather than larger pushes closer to the deadline.
* Starting on features earlier to leave time for stretch goals like summary stats and longest streak.
* Moving inline HTML styles into dedicated CSS classes for better code maintainability.

Here are changes we plan to implement in future work:
* A global heatmap showing completion history across all habits in one unified view.
* Dashboard summary stats showing overall habit performance at a glance.
* Longest streak record per habit to highlight personal bests.
* Motivational quotes displayed on habit completion.
* Potential mobile app conversion for broader accessibility.
