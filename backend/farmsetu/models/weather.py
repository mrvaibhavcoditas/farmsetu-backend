from django.db import models
from django.utils.translation import pgettext_lazy
from . import Base


class Weather(Base):
    year = models.ForeignKey(
        'Year',
        verbose_name=pgettext_lazy('field', 'Year'),
        related_name='year_weather',
        on_delete=models.CASCADE
    )
    region = models.ForeignKey(
        'Region',
        verbose_name=pgettext_lazy('field', 'Region'),
        related_name='region_weather',
        on_delete=models.CASCADE
    )
    parameter = models.ForeignKey(
        'Parameter',
        verbose_name=pgettext_lazy('field', 'Parameter'),
        related_name='parameter_weather',
        on_delete=models.CASCADE
    )
    jan = models.FloatField(
        blank=True,
        null=True
    )
    feb = models.FloatField(
        blank=True,
        null=True
    )
    mar = models.FloatField(
        blank=True,
        null=True
    )
    apr = models.FloatField(
        blank=True,
        null=True
    )
    may = models.FloatField(
        blank=True,
        null=True
    )
    jun = models.FloatField(
        blank=True, null=True
    )
    jul = models.FloatField(
        blank=True,
        null=True
    )
    aug = models.FloatField(
        blank=True,
        null=True
    )
    sep = models.FloatField(
        blank=True,
        null=True
    )
    oct = models.FloatField(
        blank=True,
        null=True
    )
    nov = models.FloatField(
        blank=True,
        null=True
    )
    dec = models.FloatField(
        blank=True,
        null=True
    )
    win = models.FloatField(
        blank=True,
        null=True
    )
    spr = models.FloatField(
        blank=True,
        null=True
    )
    sum = models.FloatField(
        blank=True,
        null=True
    )
    aut = models.FloatField(
        blank=True,
        null=True
    )
    ann = models.FloatField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('year', 'parameter', 'region')
