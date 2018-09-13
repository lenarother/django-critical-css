from unittest import mock

import pytest
from django.conf import settings

from critical.utils import complete_url


@mock.patch('critical.utils.Site.objects.get_current')
@pytest.mark.django_db
def test_complete_url_secure(site_mock, admin_user):
    class SiteMock:
        domain = 'test.com'
    settings.SESSION_COOKIE_SECURE = True
    site_mock.return_value = SiteMock()
    assert complete_url('/') == 'https://test.com/'
    assert complete_url('/foo/bar/1/') == 'https://test.com/foo/bar/1/'


@mock.patch('critical.utils.Site.objects.get_current')
@pytest.mark.django_db
def test_complete_url_unsecure(site_mock, admin_user):
    class SiteMock:
        domain = 'test.com'
    settings.SESSION_COOKIE_SECURE = False
    site_mock.return_value = SiteMock()
    assert complete_url('/') == 'http://test.com/'
    assert complete_url('/foo/bar/1/') == 'http://test.com/foo/bar/1/'
