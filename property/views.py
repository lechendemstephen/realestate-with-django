from django.shortcuts import render # type: ignore

# Create your views here.

def property(request): 

    return render(request, 'realestate/pages/property.html')

def add_property(request): 

    return render(request, 'realestate/pages/add_property.html')

def single_property(request):

    return render(request, 'realestate/pages/single_property.html')