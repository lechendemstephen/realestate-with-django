from django.db import models # type: ignore

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50)
    des = models.TextField(max_length=500)
    cat_image = models.ImageField(upload_to='category/',)
    slug = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'