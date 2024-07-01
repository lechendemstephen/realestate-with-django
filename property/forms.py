from django.forms import forms # type: ignore
from .models import Property

class Form(forms.Form):

    class Meta: 
        model = Property
        fields = ('name', 'category', 'address', 'size', 'description', 'image', 'number_of_beds', 'number_of_baths',
                  'normal_price', 'sale_price', 'agent' )
    
