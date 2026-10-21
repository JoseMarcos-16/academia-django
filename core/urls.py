from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('turmas/', views.turmas),
]