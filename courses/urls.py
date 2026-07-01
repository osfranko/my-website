from django.urls import path
from .views import create_course, course_detail

urlpatterns = [
    path('create-course/', create_course, name='create_course'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
]