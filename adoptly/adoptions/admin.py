from django.contrib import admin
from .models import Animal, AdoptionRequest, CustomUser

admin.site.register(Animal)
admin.site.register(AdoptionRequest)
admin.site.register(CustomUser)