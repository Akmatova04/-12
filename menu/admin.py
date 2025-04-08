# admin.py
from django.contrib import admin
from .models import Cake, Coffee, Drink

admin.site.register(Cake)
admin.site.register(Coffee)
admin.site.register(Drink)
