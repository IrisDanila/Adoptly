from django.contrib import admin
from .models import Animal, AdoptionRequest

admin.site.register(Animal)
admin.site.register(AdoptionRequest)