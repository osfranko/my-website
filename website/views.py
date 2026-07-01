from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, "website/home.html")


def services(request):
    return render(request, "website/services.html")


def programs(request):
    return render(request, "website/programs.html")


def stats(request):
    return render(request, "website/stats.html")


def testimonials(request):
    return render(request, "website/testimonials.html")


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            program=request.POST.get("program"),
            message=request.POST.get("message")
        )
        return render(request, "website/success.html")

    return render(request, "website/contact.html")


def dashboard(request):
    contacts = Contact.objects.all().order_by('-id')
    return render(request, "website/dashboard.html", {"contacts": contacts})