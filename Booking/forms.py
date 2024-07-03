from django import forms # type: ignore
from .models import Bookings, Payments

class BookingForm(forms.ModelForm): 
    class Meta: 
        model = Bookings
        fields = "__all__"

class PaymentForm(forms.ModelForm): 
    class Meta: 
        model = Payments
        fields = "__all__"