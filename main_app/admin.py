from django.contrib import admin
from .models import Animal, Group, Location

# Register your models here.
admin.site.register(Animal)
admin.site.register(Group)
admin.site.register(Location)
