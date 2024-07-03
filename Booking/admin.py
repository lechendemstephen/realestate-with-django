from django.contrib import admin # type: ignore
from .models import Payments, Bookings
# Register your models here.

class BookingsAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'username', 'email', 'address_1', 'address_2', 'country', 'state', 
                    'zip', 'booking_date',)
    prepopulated_fields = {
        'username': ('first_name',)
    }
class PaymentAdmin(admin.ModelAdmin): 
    list_display = ('method', 'name_on_card', 'card_number', 'expiration_date', 'cvv',)






admin.site.register(Payments, PaymentAdmin)
admin.site.register(Bookings, BookingsAdmin)