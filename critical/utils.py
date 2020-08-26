from django.conf import settings
from django.contrib.sites.models import Site


def django_cms_is_present():
    """Helper for checking wheather django-cms library is installed.

    (https://github.com/divio/django-cms)

    Returns:
        True if django-cms is installed otherwise False.

    """
    try:
        import cms  # noqa

        return True
    except ImportError:
        return False


def get_url_from_request(request):
    """Helper for getting page url.

    If django-cms is installed current_page is used.

    Returns:
        Page ansolute url.

    """
    if getattr(settings, 'CRITICAL_CSS_IGNORE_QUERY_STRING', False):
        return request.path
    return request.get_full_path()


def complete_url(url):
    """Helper for getting full uri."""
    if url.startswith('http'):
        return url
    return '{scheme}://{domain}/{url}'.format(
        scheme='https' if settings.SESSION_COOKIE_SECURE else 'http',
        domain=Site.objects.get_current().domain.rstrip('/'),
        url=url.lstrip('/'),
    )


def use_critical_css_for_request(request):
    """Check whether to use critical-css for requested page.

    Check whether critical-css is active (configured in settings) and whether
    page is published. Page drafts are always loaded without critical css.

    """
    if not getattr(settings, 'CRITICAL_CSS_ACTIVE', True):
        return False
    if django_cms_is_present():
        if (
            not request.current_page.is_published(settings.LANGUAGE_CODE)
            or request.current_page.publisher_is_draft
        ):
            return False
    return True
