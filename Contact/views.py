from django.shortcuts import render, redirect # type: ignore
from .forms import ContactForm
from .models import Contacts
from django.contrib import messages # type: ignore
# Create your views here.


def contact(request):
    if request.method == "POST": 
        form = ContactForm(request.POST)
        if form.is_valid(): 
            try:
                contact = Contacts(
                    name = form.cleaned_data.POST['name'],
                    email = form.cleaned_data.POST['email'],
                    subject = form.cleaned_data.POST['subject'],
                    message = form.cleaned_data.POST['message'],
                )
                contact.save()
                messages.success(request, 'Thank you for Contacting our customer service will be available soon')


                return redirect('contact')
                
            


            except: 
                pass


    return render(request, 'realestate/pages/contact.html')
