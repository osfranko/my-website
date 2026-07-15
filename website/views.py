from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
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
            message=request.POST.get("message"),
        )

        return render(request, "website/success.html")

    return render(request, "website/contact.html")


@staff_member_required
def dashboard(request):
    search_query = request.GET.get("search", "").strip()
    program_filter = request.GET.get("program", "").strip()

    contacts = Contact.objects.all().order_by("-created_at")

    if search_query:
        contacts = contacts.filter(
            Q(name__icontains=search_query)
            | Q(phone__icontains=search_query)
            | Q(email__icontains=search_query)
            | Q(program__icontains=search_query)
            | Q(message__icontains=search_query)
        )

    if program_filter:
        contacts = contacts.filter(program=program_filter)

    all_contacts = Contact.objects.all()

    programs = (
        all_contacts
        .exclude(program__isnull=True)
        .exclude(program="")
        .values_list("program", flat=True)
        .distinct()
        .order_by("program")
    )

    context = {
        "contacts": contacts,
        "total_contacts": all_contacts.count(),
        "search_query": search_query,
        "program_filter": program_filter,
        "programs": programs,
    }

    return render(
        request,
        "website/dashboard.html",
        context,
    )