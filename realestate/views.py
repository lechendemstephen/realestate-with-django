from django.shortcuts import render # type: ignore
from property.models import Property


def home(request):
    property = Property.objects.all()

    context = {
        'properties': property
    }


    return render(request, 'realestate/pages/index.html', context)

def about(request):


    return render(request, 'realestate/pages/about.html')

def contact(request):

    return render(request, 'realestate/pages/contact.html')