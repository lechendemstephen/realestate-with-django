from django.shortcuts import render # type: ignore
from property.models import Property
from  agents.models import Agent


def home(request):
    property = Property.objects.all()
    agent = Agent.objects.all()

    context = {
        'properties': property,
        'agents': agent,
    }


    return render(request, 'realestate/pages/index.html', context)

def about(request):


    return render(request, 'realestate/pages/about.html')

def contact(request):

    return render(request, 'realestate/pages/contact.html')