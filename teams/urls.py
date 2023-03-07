from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.get_teams, name='teams'),
    path('<str:pk>/', views.get_team, name='team'),
]