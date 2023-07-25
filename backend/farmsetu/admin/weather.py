from django.contrib import admin
from farmsetu.models import Weather



class WeatherAdmin(admin.ModelAdmin):
    list_display = ('parameter', 'region')

admin.site.register(Weather, WeatherAdmin)
