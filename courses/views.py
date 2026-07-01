from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import CourseForm
from .models import Course


# -----------------------------
# CREATE COURSE (TEACHERS ONLY)
# -----------------------------
@login_required
def create_course(request):
    profile = request.user.profile

    # block students
    if profile.user_type != 'teacher':
        return HttpResponseForbidden("Only teachers can create courses")

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('dashboard')
    else:
        form = CourseForm()

    return render(request, 'courses/create_course.html', {'form': form})


# -----------------------------
# COURSE DETAIL PAGE
# -----------------------------
def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)
    return render(request, 'courses/course_detail.html', {'course': course})