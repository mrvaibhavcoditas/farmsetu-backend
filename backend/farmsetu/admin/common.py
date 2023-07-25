from django.contrib import admin
from farmsetu.models import Parameter, Year, Region, ParameterRegion


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Parameter, ParameterAdmin)


class YearAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Year, YearAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Region, RegionAdmin)


class ParameterRegionAdmin(admin.ModelAdmin):
    list_display = ('parameter', 'region', 'url')

admin.site.register(ParameterRegion, ParameterRegionAdmin)
