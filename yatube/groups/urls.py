from django.urls import path

from . import views

urlpatterns = [
    path('groups/', views.index),
    path('groups/<int:pk>/', views.group_posts),
]