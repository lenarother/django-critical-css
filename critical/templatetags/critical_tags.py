import logging

from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from ..models import Critical
from ..tasks import calculate_critical_css


register = template.Library()
logger = logging.getLogger(__name__)

# TODO: change request.current_page.get_absolute_url()
# as it will work only for cms pages


def critical_css_is_active(request):
    """
    Check if page is published as only published pages
    shuld be displayed with critical css. For non-cms pages returns True.
    """
    if not settings.CRITICAL_CSS_ACTIVE:
        return False
    try:
        import cms  # noqa
        # For django-cms pages only published pages have critical css
        # as editors need to see changes made to the page.
        if (request.current_page.is_published(settings.LANGUAGE_CODE) and
                not request.current_page.publisher_is_draft):
            return True
    except ImportError:
        return True
    return False


@register.inclusion_tag('critical/critical.html', takes_context=True)
def critical_css(context, path):
    request = context['request']
    result_css = None
    original_path = path
    path = staticfiles_storage.url(path)

    if critical_css_is_active(request):
        url = request.current_page.get_absolute_url()
        critical, created = Critical.objects.get_or_create(url=url)
        if created:
            logger.info(
                'Templatetag: critical object created ({0})'.format(url))

        if not critical.css or critical.path != path:
            critical.path = path
            critical.css = None
            critical.save()
            calculate_critical_css.delay(
                critical_id=critical.id, original_path=original_path)
            logger.info(
                'Templatetag: triggered css calculation ({0}, {1})'.format(
                    request.current_page.pk, url))
        else:
            result_css = critical.css

    return {
        'critical_css': result_css,
        'css_path': path,
    }
