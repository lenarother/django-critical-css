from django.conf import settings
from django.contrib.sites.models import Site


def django_cms_is_present():
    """Helper for checking wheather django-cms library is present.

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
    if django_cms_is_present:
        return request.current_page.get_absolute_url()
    return request.get_full_path()


def complete_url(url):
    """Helper for getting full uri."""
    if url.startswith('http'):
        return url
    return '{scheme}://{domain}/{url}'.format(
        scheme='https' if settings.SESSION_COOKIE_SECURE else 'http',
        domain=Site.objects.get_current().domain.rstrip('/'),
        url=url.lstrip('/')
    )
