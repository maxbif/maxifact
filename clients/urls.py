from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
