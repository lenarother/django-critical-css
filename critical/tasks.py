import logging

from django.utils.safestring import mark_safe
from django_rq import job
from inline_static.css import transform_css_urls

logger = logging.getLogger(__name__)


@job
def calculate_critical_css(critical_id, original_path):
    from .exceptions import CriticalException
    from .models import Critical
    from .services import calculate_critical_css as service_calculate

    logger.info('Task: critical css with id {0} requested.'.format(critical_id))
    critical = Critical.objects.filter(id=critical_id).first()
    if not critical:
        raise CriticalException('There is no Critical object with id {0}'.format(critical_id))
    logger.info('Task: {0}, {1}'.format(critical.url, critical.path))

    critical.is_pending = True
    critical.save(update_fields=['is_pending'])
    logger.info('Task: critical css with id {0} pending.'.format(critical_id))

    try:
        critical_css_raw = service_calculate(critical.url, critical.path)
        critical_css = transform_css_urls(original_path, critical.path, critical_css_raw)
    except Exception as exc:
        critical.is_pending = False
        critical.save(update_fields=['is_pending'])
        raise CriticalException('Could not calculate critical css') from exc

    critical.css = mark_safe(critical_css)
    critical.is_pending = False
    critical.save()
    logger.info('Task: critical css with id {0} saved.'.format(critical_id))
