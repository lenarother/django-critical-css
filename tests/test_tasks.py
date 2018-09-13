# TODO
# from unittest import mock
#
# import pytest
# from cms.api import create_page, publish_page
#
# from critical.exceptions import CriticalException, PenthouseException
# from critical.models import Critical
# from critical.tasks import calculate_critical_css
#
#
# @pytest.mark.django_db
# def test_critical_no_object(admin_user):
#     with pytest.raises(CriticalException):
#         calculate_critical_css(18, 'css/styles.css')
#         calculate_critical_css('foo', 'css/styles.css')
#
#
# @mock.patch('critical.api.PenthouseApi.get_critical_css')
# @pytest.mark.django_db
# def test_critical_created_after_page_publish(api_mock, admin_user):
#     api_mock.return_value = 'testing-task'
#     page = create_page('page', 'INHERIT', 'de')
#     publish_page(page, admin_user, 'de')
#     critical = Critical.objects.first()
#     assert critical.css is None
#
#     calculate_critical_css(critical.id, 'css/styles.css')
#     critical.refresh_from_db()
#     assert api_mock.call_count == 1
#     assert critical.css == 'testing-task'
#     assert critical.is_pending is False
#
#
# @mock.patch('critical.api.PenthouseApi.get_critical_css')
# @pytest.mark.django_db
# def test_css_paths_transformation(api_mock, admin_user, settings):
#     settings.STATIC_URL = '/foobar/'
#     api_mock.return_value = '.myclass{url("../img/logo.svg");}'
#     page = create_page('page', 'INHERIT', 'de')
#     publish_page(page, admin_user, 'de')
#     critical = Critical.objects.first()
#     assert critical.css is None
#
#     calculate_critical_css(critical.id, 'css/styles.css')
#     critical.refresh_from_db()
#     assert api_mock.call_count == 1
#     assert critical.css == '.myclass{url("/foobar/img/logo.svg");}'
#     assert critical.is_pending is False
#
#
# @mock.patch('critical.api.PenthouseApi')
# @pytest.mark.django_db
# def test_api_exception(api_mock, admin_user, settings):
#     settings.STATIC_URL = '/foobar/'
#     api_mock.side_effect = PenthouseException()
#     page = create_page('page', 'INHERIT', 'de')
#     publish_page(page, admin_user, 'de')
#     with pytest.raises(CriticalException):
#         critical = Critical.objects.first()
#         calculate_critical_css(critical.id, 'css/styles.css')
#
#     critical.refresh_from_db()
#     assert api_mock.call_count == 1
#     assert critical.css is None
#     assert critical.is_pending is False
