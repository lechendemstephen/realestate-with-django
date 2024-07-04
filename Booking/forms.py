from django import forms # type: ignore
from .models import Bookings, Payments

class BookingForm(forms.ModelForm): 
    class Meta: 
        model = Bookings
        fields = ('first_name', 'last_name', 'username',  'email', 'address_1', 'address_2', 'country', 'state', 'zip')

class PaymentForm(forms.ModelForm): 
    class Meta: 
        model = Payments
        fields = ('method', 'name_on_card', 'card_number', 'expiration_date', 'cvv')