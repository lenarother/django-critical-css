from unittest import mock

import pytest

from critical.exceptions import CriticalException, PenthouseException
from critical.models import Critical
from critical.tasks import calculate_critical_css

from .factories import CriticalFactory


@pytest.mark.django_db
def test_critical_no_object(admin_user):
    Critical.objects.all().delete()
    with pytest.raises(CriticalException):
        calculate_critical_css(18, 'css/styles.css')


@mock.patch('critical.api.PenthouseApi.get_critical_css')
@pytest.mark.django_db
def test_penthouse_api_called(api_mock):
    api_mock.return_value = 'testing-task'
    critical = CriticalFactory.create(
        url='/', path='/static/css/styles.css', css=None)

    calculate_critical_css(critical.id, 'css/styles.css')
    critical.refresh_from_db()

    assert api_mock.call_count == 1
    api_mock.assert_called_with('/', '/static/css/styles.css')
    assert critical.css == 'testing-task'
    assert critical.is_pending is False


@mock.patch('critical.api.PenthouseApi.get_critical_css')
@pytest.mark.django_db
def test_css_paths_transformation(api_mock, settings):
    settings.STATIC_URL = '/foobar/'
    api_mock.return_value = '.myclass{url("../img/logo.svg");}'
    critical = CriticalFactory.create(
        url='/', path='/static/css/styles.css', css=None)

    calculate_critical_css(critical.id, 'css/styles.css')
    critical.refresh_from_db()
    assert critical.css == '.myclass{url("/foobar/img/logo.svg");}'
    assert critical.is_pending is False


@mock.patch('critical.api.PenthouseApi')
@pytest.mark.django_db
def test_penthouse_api_errror(api_mock, admin_user, settings):
    api_mock.side_effect = PenthouseException()
    critical = CriticalFactory.create(
        url='/', path='/static/css/styles.css', css=None)

    with pytest.raises(CriticalException):
        calculate_critical_css(critical.id, 'css/styles.css')

    critical.refresh_from_db()
    assert critical.css is None
    assert critical.is_pending is False
