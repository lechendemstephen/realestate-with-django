from django.db import models # type: ignore

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    contact_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

    class Meta: 
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'