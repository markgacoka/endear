from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('morality-of-war/', views.war, name='war'),
    path('solution/', views.solution, name='solution'),
    path('error/', views.login_error, name='login_error'),
]