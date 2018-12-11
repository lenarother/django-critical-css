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


def test_use_critical_css_for_request(settings, rf):
    settings.CRITICAL_CSS_ACTIVE = False
    request = rf.get('/')
    assert use_critical_css_for_request(request) is False


@pytest.mark.cms
@pytest.mark.django_db
def test_use_critical_css_for_request_with_cms(settings, rf, admin_user):
    settings.CRITICAL_CSS_ACTIVE = True
    page = create_page('page', 'INHERIT', 'de')
    request = rf.get('/page')
    request.current_page = page
    assert use_critical_css_for_request(request) is False

    publish_page(page, admin_user, 'de')
    page.refresh_from_db()
    request = rf.get('/page')
    request.current_page = page
    assert use_critical_css_for_request(request) is True

    request = rf.get('/page')
    request.current_page = page.get_draft_object()
    assert use_critical_css_for_request(request) is False
