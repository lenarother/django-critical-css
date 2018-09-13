# TODO
# import pytest
# from cms.api import create_page, get_page_draft, publish_page
#
# from critical.models import Critical
#
#
# @pytest.mark.django_db
# class TestSignals:
#
#     def test_critical_created_after_page_publish(self, admin_user):
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         critical = Critical.objects.first()
#
#         assert Critical.objects.count() == 1
#         assert critical.url == page.get_absolute_url()
#         assert critical.path is None
#         assert critical.css is None
#
#     def test_critical_updated_after_page_publish(self, admin_user):
#         page = create_page('page', 'INHERIT', 'de')
#         publish_page(page, admin_user, 'de')
#         critical = Critical.objects.first()
#         critical.path = 'css/styles.css'
#         critical.css = 'test-critical-css'
#         critical.save()
#
#         draft = get_page_draft(page)
#         draft.publish('de')
#         critical.refresh_from_db()
#
#         assert Critical.objects.count() == 1
#         assert critical.path == 'css/styles.css'
#         assert critical.css is None
