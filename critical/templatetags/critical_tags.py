import logging

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

from ..models import Critical
from ..tasks import calculate_critical_css
from ..utils import get_url_from_request, use_critical_css_for_request

register = template.Library()
logger = logging.getLogger(__name__)


@register.inclusion_tag('critical/critical.html', takes_context=True)
def critical_css(context, path):
    request = context['request']
    result_css = None
    original_path = path
    path = staticfiles_storage.url(path)

    if use_critical_css_for_request(request):
        url = get_url_from_request(request)
        critical, created = Critical.objects.get_or_create(url=url)
        if created:
            logger.info('Templatetag: critical object created ({0})'.format(url))

        if not critical.css or critical.path != path:
            critical.path = path
            critical.css = None
            critical.save()
            calculate_critical_css.delay(critical_id=critical.id, original_path=original_path)
            logger.info('Templatetag: triggered css calculation for {0}'.format(url))
        result_css = critical.css

    return {'critical_css': result_css, 'css_path': path}
