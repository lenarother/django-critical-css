from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .utils import django_cms_is_present


class CriticalConfig(AppConfig):
    name = 'critical'
    verbose_name = _('CriticalCSS')

    def ready(self):
        if django_cms_is_present():
            # Include signals for refreshing critical css on page publish
            import critical.signals.handlers  # noqa
