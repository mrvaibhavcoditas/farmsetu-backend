from django.db import models
from django.utils.translation import pgettext_lazy

from django.conf import settings


class Base(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=pgettext_lazy('field', 'Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=pgettext_lazy('field', 'Updated at')
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=pgettext_lazy('field', 'Created by'),
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=pgettext_lazy('field', 'Updated by'),
        on_delete=models.CASCADE,
        related_name='%(class)s_updated_by',
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
