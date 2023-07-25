from django.db import models
from django.utils.translation import pgettext_lazy
from . import Base


class Year(Base):
    name = models.IntegerField(
        unique=True,
        verbose_name=pgettext_lazy('field', 'Year')
    )

    # def __str__(self):
    #     return self.name


class Parameter(Base):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=pgettext_lazy('field', 'Parameter')
    )

    def __str__(self):
        return self.name


class Region(Base):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=pgettext_lazy('field', 'Name')
    )

    def __str__(self):
        return self.name


class ParameterRegion(Base):
    parameter = models.ForeignKey(
        'Parameter',
        verbose_name=pgettext_lazy('field', 'Parameter'),
        related_name='parameter_regions',
        on_delete=models.CASCADE
    )
    region = models.ForeignKey(
        'Region',
        verbose_name=pgettext_lazy('field', 'Parameter'),
        related_name='region_parameters',
        on_delete=models.CASCADE
    )
    url = models.URLField(
        verbose_name=pgettext_lazy('field', 'URL')
    )

    class Meta:
        unique_together = ('parameter', 'region')
