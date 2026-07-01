from django.contrib import admin
from .models import Contact


# ================= CONTACT ADMIN =================
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'program', 'created_at')
    list_filter = ('program', 'created_at')
    search_fields = ('name', 'phone', 'email', 'program')


admin.site.register(Contact, ContactAdmin)