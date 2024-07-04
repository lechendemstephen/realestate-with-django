from django.contrib import admin # type: ignore
from .models import Contacts
# Register your models here.

class ContactAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'subject', 'message', 'contact_date')


admin.site.register(Contacts, ContactAdmin)