from django.conf import settings
from django.contrib.sites.models import Site


def complete_url(url):
    if url.startswith('http'):
        return url
    return '{scheme}://{domain}/{url}'.format(
        scheme='https' if settings.SESSION_COOKIE_SECURE else 'http',
        domain=Site.objects.get_current().domain.rstrip('/'),
        url=url.lstrip('/')
    )
