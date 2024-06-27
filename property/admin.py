from django.contrib import admin # type: ignore
from .models import Property
# Register your models here.

class PropertyAdmin(admin.ModelAdmin): 
    list_display = ('name', 'category', 'slug', 'address', 'size', 'description', 'image', 'number_of_beds', 'number_of_baths', 'normal_price', 'sale_price', 'agent', 'created_date')
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Property, PropertyAdmin)
