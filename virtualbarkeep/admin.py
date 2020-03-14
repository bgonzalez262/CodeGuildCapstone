from django.contrib import admin
from .models import Event, SavedDrink, SavedFood, EventItems

# Register your models here.
admin.site.register(Event)
admin.site.register(SavedFood)
admin.site.register(SavedDrink)
admin.site.register(EventItems)
