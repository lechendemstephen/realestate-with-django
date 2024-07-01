from django.db import models # type: ignore
from category.models import Category
from agents.models import Agent
from django.urls import reverse # type: ignore
# Create your models here.

class Property(models.Model): 
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    size = models.IntegerField()
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='property/',)
    number_of_beds = models.IntegerField()
    number_of_baths = models.IntegerField()
    normal_price = models.IntegerField()
    sale_price = models.IntegerField()
    slug = models.CharField(max_length=150)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
    class Meta: 
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def property_url(self): 

        return reverse('single_property', args=[self.slug])
    
