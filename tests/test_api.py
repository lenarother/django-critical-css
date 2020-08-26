from unittest import mock

import pytest
import requests
from django.contrib.sites.models import Site

from critical.api import (
    PenthouseApi,
    PenthouseException,
    calculate_critical_css,
)


@pytest.mark.django_db
class TestPenthouseApi:
    def test_base_url(self, settings):
        settings.PENTHOUSE_URL = 'http://foobar:3000/'
        api = PenthouseApi()
        assert api.base_url == 'http://foobar:3000/'

    def test_base_url_error(self, settings):
        settings.PENTHOUSE_URL = None
        api = PenthouseApi()
        with pytest.raises(PenthouseException):
            api.base_url

    def test_get_params(self, settings):
        settings.SESSION_COOKIE_SECURE = False
        settings.PENTHOUSE_CONFIG = {'width': '100'}
        site = Site.objects.create(domain='test.com')
        settings.SITE_ID = site.id

        api = PenthouseApi()

        assert api.get_params('/foo', 'css/test.css') == (
            {
                'css': 'http://test.com/css/test.css',
                'url': 'http://test.com/foo',
                'width': '100',
            }
        )

    def test_get_params_no_config(self, settings):
        settings.SESSION_COOKIE_SECURE = False
        del settings.PENTHOUSE_CONFIG
        site = Site.objects.create(domain='test.com')
        settings.SITE_ID = site.id

        api = PenthouseApi()

        assert api.get_params('/foo', 'css/test.css') == (
            {'css': 'http://test.com/css/test.css', 'url': 'http://test.com/foo'}
        )

    @mock.patch('critical.api.requests.get')
    def test_request_critical_css(self, requests_get_mock, settings):
        class ResponseMock:
            status_code = 200
            text = 'foo'
            url = 'http://foo.bar.com'

            def raise_for_status(self):
                return False

        settings.PENTHOUSE_URL = 'http://foobar:3000/'
        settings.PENTHOUSE_CONFIG = {}
        settings.SESSION_COOKIE_SECURE = False
        site = Site.objects.create(domain='test.com')
        settings.SITE_ID = site.id
        requests_get_mock.return_value = ResponseMock()

        api = PenthouseApi()
        api.request_critical_css('/foo', 'css/test.css')

        requests_get_mock.assert_called_once_with(
            'http://foobar:3000/',
            {'url': 'http://test.com/foo', 'css': 'http://test.com/css/test.css'},
        )

    @mock.patch('critical.api.requests.get')
    def test_request_critical_css_raises(self, requests_get_mock, settings):
        settings.PENTHOUSE_URL = 'http://foobar:3000/'
        settings.SESSION_COOKIE_SECURE = False
        site = Site.objects.create(domain='test.com')
        settings.SITE_ID = site.id
        requests_get_mock.side_effect = requests.RequestException()

        api = PenthouseApi()

        with pytest.raises(PenthouseException):
            api.request_critical_css('/foo', 'css/test.css')

    @mock.patch('critical.api.requests.get')
    def test_request_critical_css_raises_invalid_status(self, requests_get_mock):
        class ResponseMock:
            status_code = 401
            text = 'foo'
            url = 'http://foo.bar.com'

            def raise_for_status(self):
                return False

        requests_get_mock.return_value = ResponseMock()

        api = PenthouseApi()

        with pytest.raises(PenthouseException):
            api.request_critical_css('/foo', 'css/test.css')

    @mock.patch('critical.api.requests.get')
    def test_get_critical_css(self, requests_get_mock):
        class ResponseMock:
            status_code = 200
            text = 'foo'
            url = 'http://foo.bar.com'

            def raise_for_status(self):
                return False

        requests_get_mock.return_value = ResponseMock()

        api = PenthouseApi()
        css = api.get_critical_css('/foo', 'css/test.css')
        assert css == 'foo'

    @mock.patch('critical.api.requests.get')
    def test_get_critical_css_raises_error_in_text(self, requests_get_mock):
        class ResponseMock:
            status_code = 200
            text = '401 Unauthorized\n'
            url = 'http://foo.bar.com'

            def raise_for_status(self):
                return False

        requests_get_mock.return_value = ResponseMock()

        api = PenthouseApi()

        with pytest.raises(PenthouseException):
            api.get_critical_css('/foo', 'css/test.css')


@mock.patch('critical.api.PenthouseApi.get_critical_css')
def test_calculate_critical_css(get_critical_css_mock):
    calculate_critical_css('https://foo/bar.com', 'https://foo/bar.css')
    assert get_critical_css_mock.call_count == 1
