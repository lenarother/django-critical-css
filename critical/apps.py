from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .utils import django_cms_is_present


class CriticalConfig(AppConfig):
    name = 'critical'
    verbose_name = _('CriticalCSS')

    def ready(self):
        # Signals for handling critical css for cms pages
        # are installed only if django-cms is present.
        if django_cms_is_present():
            import critical.signals.handlers  # noqa
