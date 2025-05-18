from django.contrib import admin

from .models import Incident, Location, Firefighters, FireStation, FireTruck, WeatherConditions

admin.site.register(Incident)
admin.site.register(Location)
admin.site.register(Firefighters)
admin.site.register(FireStation)
admin.site.register(FireTruck)
admin.site.register(WeatherConditions)
