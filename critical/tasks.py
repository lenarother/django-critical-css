import logging

from barbeque.staticfiles.css import transform_css_urls
from django.utils.safestring import mark_safe
from django_rq import job


logger = logging.getLogger(__name__)


@job
def calculate_critical_css(critical_id, original_path):
    from .api import PenthouseApi
    from .exceptions import CriticalException, PenthouseException
    from .models import Critical

    logger.info('Task: critical css with id {0} requested.'.format(critical_id))
    critical = Critical.objects.filter(id=critical_id).first()
    if not critical:
        raise CriticalException(
            'There is no Critical object with id {0}'.format(critical_id))
    logger.info('Task: {0}, {1}'.format(critical.url, critical.path))

    critical.is_pending = True
    critical.save(update_fields=['is_pending'])
    logger.info('Task: critical css with id {0} pending.'.format(critical_id))

    try:
        api = PenthouseApi()
        critical_css_raw = api.get_critical_css(critical.url, critical.path)
    except PenthouseException as error:
        critical.is_pending = False
        critical.save(update_fields=['is_pending'])
        raise CriticalException('PenthouseException: {0}'.format(error))

    critical_css = transform_css_urls(
        original_path, critical.path, critical_css_raw)
    critical.css = mark_safe(critical_css)
    critical.is_pending = False
    critical.save()
    logger.info('Task: critical css with id {0} saved.'.format(critical_id))
