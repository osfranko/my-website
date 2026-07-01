from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Profile
from courses.models import Course


def home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def dashboard(request):
    profile = request.user.profile

    if profile.user_type == 'teacher':
        courses = Course.objects.filter(teacher=request.user)
        return render(request, 'accounts/teacher_dashboard.html', {
            'courses': courses
        })
    else:
        courses = Course.objects.all()
        return render(request, 'accounts/student_dashboard.html', {
            'courses': courses
        })