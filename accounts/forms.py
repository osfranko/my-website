from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']