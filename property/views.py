from django.shortcuts import render # type: ignore
from .models import Property
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

    context ={
        'property': property,
    }

    return render(request, 'realestate/pages/booking.html', context)