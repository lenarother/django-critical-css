from unittest import mock

import pytest
from django.template import Context, Template

from critical.models import Critical

from .factories import CriticalFactory


@pytest.mark.django_db
class TestCriticalTags:
    @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
    @mock.patch('critical.templatetags.critical_tags.use_critical_css_for_request')
    def test_dont_use_critical(self, use_critical_mock, critical_task_mock, rf):
        use_critical_mock.return_value = False
        request = rf.get('/')

        context = Context({'request': request})
        template_to_render = Template(
            '{% load critical_tags %}' '{% critical_css "css/styles.css" %}'
        )

        assert Critical.objects.count() == 0

        rendered_template = template_to_render.render(context)

        assert critical_task_mock.delay.call_count == 0
        assert Critical.objects.count() == 0
        assert rendered_template.strip() == (
            '<link rel="stylesheet" type="text/css" ' 'href="/static/css/styles.css" />'
        )

    @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
    @mock.patch('critical.templatetags.critical_tags.use_critical_css_for_request')
    def test_critical_object_created(self, use_critical_mock, critical_task_mock, rf):
        use_critical_mock.return_value = True
        critical_task_mock.delay.return_value = 'foo bar bazz'
        request = rf.get('/')

        context = Context({'request': request})
        template_to_render = Template(
            '{% load critical_tags %}' '{% critical_css "css/styles.css" %}'
        )

        assert Critical.objects.count() == 0

        rendered_template = template_to_render.render(context)

        assert critical_task_mock.delay.call_count == 1
        assert Critical.objects.count() == 1
        assert rendered_template.strip() == (
            '<link rel="stylesheet" type="text/css" ' 'href="/static/css/styles.css" />'
        )

    @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
    @mock.patch('critical.templatetags.critical_tags.use_critical_css_for_request')
    def test_success(self, use_critical_mock, critical_task_mock, rf):
        use_critical_mock.return_value = True
        request = rf.get('/')
        CriticalFactory.create(url='/', path='/static/css/styles.css', css='foo bar')

        context = Context({'request': request})
        template_to_render = Template(
            '{% load critical_tags %}' '{% critical_css "css/styles.css" %}'
        )

        rendered_template = template_to_render.render(context)
        assert '<style type="text/css">foo bar</style>' in rendered_template
        assert critical_task_mock.delay.call_count == 0

    @mock.patch('critical.templatetags.critical_tags.calculate_critical_css')
    @mock.patch('critical.templatetags.critical_tags.use_critical_css_for_request')
    def test_wrong_path(self, use_critical_mock, critical_task_mock, rf):
        use_critical_mock.return_value = True
        request = rf.get('/')

        CriticalFactory.create(url='/', path='/static/css/styles.css', css='foo bar')

        context = Context({'request': request})
        template_to_render = Template(
            '{% load critical_tags %}' '{% critical_css "css/other_styles.css" %}'
        )

        rendered_template = template_to_render.render(context)
        assert critical_task_mock.delay.called is True
        assert rendered_template.strip() == (
            '<link rel="stylesheet" type="text/css" ' 'href="/static/css/other_styles.css" />'
        )
