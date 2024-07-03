from django.db import models # type: ignore

# Create your models here.

class Bookings(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 

        return self.first_name
    class Meta: 
        verbose_name = 'Bookings'
        verbose_name_plural = 'Bookings'

class Payments(models.Model): 
    method = models.CharField(max_length=50)
    name_on_card = models.CharField(max_length=100)
    card_number = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    cvv = models.IntegerField()


    def __str__(self): 

        return self.method 
    
    class Meta: 
        verbose_name = 'Payments'
        verbose_name_plural = 'Payments'



