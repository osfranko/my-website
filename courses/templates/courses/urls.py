from django.urls import path
from .views import create_course

urlpatterns = [
    path('create-course/', create_course, name='create_course'),
]