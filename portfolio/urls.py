from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
    path('git-dashboard/', views.git_contribution_dashboard, name='git_dashboard'),

]