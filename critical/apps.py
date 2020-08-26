from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CriticalConfig(AppConfig):
    name = 'critical'
    verbose_name = _('CriticalCSS')

    def ready(self):
        try:
            # If django-cms is installed include signals
            # for refreshing critical css on page publish
            import cms  # noqa

            import critical.signals.handlers  # noqa
        except ImportError:
            pass
