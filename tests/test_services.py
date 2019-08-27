from unittest import mock

from critical.services import calculate_critical_css


@mock.patch('critical.api.calculate_critical_css')
def test_calculate_critical_css(calculate_critical_css_mock):
    calculate_critical_css('https://foo/bar.com', 'https://foo/bar.css')
    assert calculate_critical_css_mock.call_count == 1


@mock.patch('critical.api.calculate_critical_css')
def test_calculate_critical_css_with_custom_backend(calculate_critical_css_mock, settings):
    settings.CRITICAL_CSS_BACKEND = 'tests.resources.backend_mock.calculate_critical_css'
    assert calculate_critical_css('https://foo/bar.com', 'https://foo/bar.css') == 'foobarbazz'
    assert calculate_critical_css_mock.call_count == 0
