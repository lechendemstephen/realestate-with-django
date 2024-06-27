from django.contrib import admin # type: ignore
from .models import Agent
# Register your models here.

class AgentAdmin(admin.ModelAdmin): 
    list_display = ('name', 'address', 'phone', 'profile_picture', 'jioned_date')


admin.site.register(Agent, AgentAdmin)