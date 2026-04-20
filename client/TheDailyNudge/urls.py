"""
URL configuration for TheDailyNudge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('managehabits/', views.manage_habits, name='managehabits'),
    path('managehabits/edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('managehabits/delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('dashboard/complete/<int:habit_id>/', views.complete_habit, name='complete_habit'),
    path('dashboard/name-pet/<int:habit_id>/', views.name_pet, name='name_pet'),
]
