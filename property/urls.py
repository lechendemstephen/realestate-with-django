from django.urls import path  # type: ignore
from . import views
urlpatterns = [
    path('', views.property, name='property'),
    path('add_property/', views.add_property, name='add_property'),
    path('single_property/<slug:property_slug>/', views.single_property, name='single_property'),
    
]
