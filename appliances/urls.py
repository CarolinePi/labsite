from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.add_new, name='new'),
    path('tv/', views.tv, name='tv'),
    path('fridge/', views.fridge, name='fridge'),
    path('fridge/receiver/', views.receiver),
    path('tv/receiver/', views.receiver)
]
