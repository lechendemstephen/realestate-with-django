from django.urls import path # type: ignore
from . import views
urlpatterns = [
    
    path('', views.contact, name='contact'),

]
