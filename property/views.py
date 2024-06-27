from django.shortcuts import render # type: ignore

# Create your views here.

def property(request): 

    return render(request, 'realestate/pages/property.html')

def add_property(request): 

    return render(request, 'realestate/pages/add_property.html')