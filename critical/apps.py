from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CriticalConfig(AppConfig):
    name = 'critical'
    verbose_name = _('CriticalCSS')

    def ready(self):
        # Signals for handling critical css for cms pages
        # are installed only if django-cms is present.
        try:
            import cms  # noqa
            import critical.signals.handlers  # noqa
        except ImportError:
            pass
