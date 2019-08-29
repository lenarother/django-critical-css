from django.db import models
from django.utils.translation import ugettext_lazy as _


class Critical(models.Model):
    url = models.URLField(_('Page URL'), max_length=200, unique=True)
    path = models.CharField(_('CSS path'), max_length=255, blank=True, null=True)
    css = models.TextField(_('Critical CSS'), blank=True, null=True)
    is_pending = models.BooleanField(_('Is pending'), default=False)
    date_updated = models.DateTimeField(_('Date updated'), auto_now=True)

    class Meta:
        verbose_name = _('Critical CSS')
        verbose_name_plural = _('Critical CSS')
        ordering = ('-date_updated', 'url')

    def __str__(self):
        return self.url
