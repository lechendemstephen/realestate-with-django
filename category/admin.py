from django.contrib import admin # type: ignore
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'des', 'cat_image', 'slug', 'created_date')
    prepopulated_fields = {
        'slug': ('name',)
    }



admin.site.register(Category, CategoryAdmin)