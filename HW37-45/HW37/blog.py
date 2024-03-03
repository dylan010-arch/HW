from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about-club'),
    path('time/', views.current_datetime, name='current-time'),
    path('greet/<str:name>/', views.greet, name='greet'),
]
