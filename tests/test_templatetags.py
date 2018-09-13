# TODO
# from unittest import mock
#
# import pytest
# from cms.api import create_page, publish_page
# from django.template import Context, Template
#
# from critical.models import Critical
#
#
# @pytest.mark.django_db
# class TestCriticalTags:
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_page_not_published(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.STATIC_URL = '/static/'
#
#         page = create_page('page', 'INHERIT', 'de')
#         request = rf.get('/')
#         request.current_page = page
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "css/styles.css" %}'
#         )
#
#         assert Critical.objects.count() == 0
#
#         rendered_template = template_to_render.render(context)
#
#         assert critical_task_mock.delay.call_count == 0
#         assert Critical.objects.count() == 0
#         assert rendered_template.strip() == (
#             '<link rel="stylesheet" type="text/css" href="/static/css/styles.css" />')
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_no_css(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#         settings.CRITICAL_CSS_ACTIVE = True
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page.refresh_from_db()
#         request = rf.get('/', SERVER_NAME='example.com')
#         request.current_page = page.get_public_object()
#         critical = Critical.objects.get(url=page.get_absolute_url())
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "css/styles.css" %}'
#         )
#         rendered_template = template_to_render.render(context)
#
#         assert critical_task_mock.delay.call_count == 1
#         assert Critical.objects.count() == 1
#         assert critical.css is None
#         assert rendered_template.strip() == (
#             '<link rel="stylesheet" type="text/css" '
#             'href="/static/css/styles.css" />')
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_changed_path(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#         settings.CRITICAL_CSS_ACTIVE = True
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page.refresh_from_db()
#         request = rf.get('/', SERVER_NAME='example.com')
#         request.current_page = page.get_public_object()
#         critical = Critical.objects.get(url=page.get_absolute_url())
#         critical.css = 'foo-bar'
#         critical.path = 'css/other/styles.css'
#         critical.save(update_fields=['css', 'path'])
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "/css/styles.css" %}'
#         )
#         rendered_template = template_to_render.render(context)
#         critical.refresh_from_db()
#
#         assert critical_task_mock.delay.call_count == 1
#         assert Critical.objects.count() == 1
#         assert critical.css is None
#         assert critical.path == '/static/css/styles.css'
#         assert rendered_template.strip() == (
#             '<link rel="stylesheet" type="text/css" href="/static/css/styles.css" />')
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_success(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#         settings.CRITICAL_CSS_ACTIVE = True
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page.refresh_from_db()
#         request = rf.get('/', SERVER_NAME='example.com')
#         request.current_page = page.get_public_object()
#         critical = Critical.objects.get(url=page.get_absolute_url())
#         critical.css = 'foo-bar-bazz-critical-css'
#         critical.path = '/static/css/styles.css'
#         critical.save(update_fields=['css', 'path'])
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "css/styles.css" %}'
#         )
#         rendered_template = template_to_render.render(context)
#
#         assert critical_task_mock.delay.call_count == 0
#         assert Critical.objects.count() == 1
#         assert 'foo-bar-bazz-critical-css' in rendered_template
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_page_is_draft(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#         settings.CRITICAL_CSS_ACTIVE = True
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page.refresh_from_db()
#         request = rf.get('/', SERVER_NAME='example.com')
#         request.current_page = page.get_draft_object()
#         critical = Critical.objects.get(url=page.get_absolute_url())
#         critical.css = 'foo-bar-bazz-critical-css'
#         critical.path = '/static/css/styles.css'
#         critical.save(update_fields=['css', 'path'])
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "css/styles.css" %}'
#         )
#         rendered_template = template_to_render.render(context)
#
#         assert critical_task_mock.delay.call_count == 0
#         assert Critical.objects.count() == 1
#         assert (
#             '<link rel="stylesheet" type="text/css" href="/static/css/styles.css" />'
#             in rendered_template)
#
#     @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
#     def test_critical_css_not_active(
#             self, critical_task_mock, client, admin_user, rf, settings):
#         settings.ALLOWED_HOSTS.append('example.com')
#         settings.STATIC_URL = '/static/'
#         settings.CRITICAL_CSS_ACTIVE = False
#
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         page.refresh_from_db()
#         request = rf.get('/', SERVER_NAME='example.com')
#         request.current_page = page.get_public_object()
#         critical = Critical.objects.get(url=page.get_absolute_url())
#         critical.css = 'foo-bar-bazz-critical-css'
#         critical.path = '/static/css/styles.css'
#         critical.save(update_fields=['css', 'path'])
#
#         context = Context({'request': request})
#         template_to_render = Template(
#             '{% load critical_tags %}'
#             '{% critical_css "css/styles.css" %}'
#         )
#         rendered_template = template_to_render.render(context)
#
#         assert critical_task_mock.delay.call_count == 0
#         assert rendered_template.strip() == (
#             '<link rel="stylesheet" type="text/css" href="/static/css/styles.css" />')
