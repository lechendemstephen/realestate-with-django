from django.shortcuts import render # type: ignore



def home(request):

    return render(request, 'realestate/pages/index.html')

def about(request):


    return render(request, 'realestate/pages/about.html')

def contact(request):

    return render(request, 'realestate/pages/contact.html')