from django.shortcuts import render # type: ignore

# Create your views here.
def signup(request): 

    return render(request, 'realestate/pages/signup.html')