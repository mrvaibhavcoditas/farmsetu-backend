import django_filters
from farmsetu.models import Weather


class WeatherFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='year__name')
    parameter = django_filters.CharFilter(field_name='parameter__name')
    region = django_filters.CharFilter(field_name='region__name')

    class Meta:
        model = Weather
        fields = ['year']

