from django.shortcuts import render, redirect # type: ignore
from .models import Property
from Booking.models import Payments, Bookings
from Booking.forms import BookingForm, PaymentForm
from django.contrib import messages # type: ignore
# Create your views here.

def property(request): 

    return render(request, 'realestate/pages/property.html')





def add_property(request): 

    return render(request, 'realestate/pages/add_property.html')




def single_property(request, property_slug):

    single_property = Property.objects.filter(slug=property_slug)

    context = {
        'single_properties': single_property
    }


    return render(request, 'realestate/pages/single_property.html', context)



def book(request, property_slug): 
    property = Property.objects.get(slug=property_slug)
    form = BookingForm(request.POST)
    form1 = PaymentForm(request.POST)
    if request.method == 'POST': 
        print(True)
        if form.is_valid() and form1.is_valid():
            try: 
                booking = Bookings (
                    first_name = form.cleaned_data.get['first_name'],
                    last_name = form.cleaned_data.get['last_name'],
                    username = form.cleaned_data.get['username'],
                    email = form.cleaned_data.get['email'],
                    address_1 = form.cleaned_data.get['address_1'],
                    address_2 = form.cleaned_data.get['address_2'],
                    country = form.cleaned_data.get['country'],
                    state = form.cleaned_data.get['state'],
                    zip = form.cleaned_data.get['zip'],
                )
                payment = Payments(
                    method = form1.cleaned_data.get['credit_card'],
                    name_on_card = form1.cleaned_data.get['name_on_card'],
                    expiration_date = form1.cleaned_data.get['expiration_date'],
                    cvv = form1.cleaned_data.get['cvv']

                )
                booking.save()
                payment.save()
                messages.success(request, 'Your Reservation has been booked')

                return redirect('booking')

            except:
                pass 

    else: 
        form = BookingForm()



    context ={
        'property': property,
        'form': form,
        'form1': form1,
    }

    return render(request, 'realestate/pages/booking.html', context)


def booking(request): 
    

    return render(request, 'realestate/pages/booking.html')