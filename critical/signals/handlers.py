import logging

from cms.signals import post_publish
from django.dispatch import receiver

from ..models import Critical

logger = logging.getLogger(__name__)


@receiver(post_publish)
def set_critical_css_to_empty(sender, **kwargs):
    page = kwargs.get('instance')
    url = page.get_absolute_url()

    critical, created = Critical.objects.get_or_create(url=url)
    if not created:
        critical.css = None
        critical.save()
        logger.info('Page published signal: critical css deleted ({0})'.format(url))
    else:
        logger.info('Page published signal: critical css created ({0})'.format(url))
