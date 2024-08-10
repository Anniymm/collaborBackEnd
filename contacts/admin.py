from django.contrib import admin
from .models import contactsUs

@admin.register(contactsUs)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'time')
