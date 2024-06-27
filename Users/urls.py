from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
