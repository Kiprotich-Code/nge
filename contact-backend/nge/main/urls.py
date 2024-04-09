from django.urls import path
from . import views

# URLS for main 
urlpatterns = [
    path('', views.base, name="base")
]