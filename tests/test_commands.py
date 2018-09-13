# TODO
# from unittest import mock
#
# import pytest
# from cms.api import create_page, publish_page
# from django.core.management import call_command
#
#
# @pytest.mark.django_db
# class TestCritical:
#
#     @mock.patch('critical.api.requests.get')
#     def test_critical_css_changed_path(
#             self, requests_get_mock, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page2 = create_page('second-page', 'INHERIT', 'de')
#         publish_page(page2, admin_user, 'de')
#
#         call_command('run_critical')
#
#         assert requests_get_mock.call_count == 2
