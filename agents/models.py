from django.db import models # type: ignore

# Create your models here.
class Agent(models.Model): 
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='agents/',)
    jioned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    