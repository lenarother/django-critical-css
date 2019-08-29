import pytest


def pytest_report_header(config):
    try:
        import cms  # noqa
        cms_present = True
    except ImportError:
        cms_present = False

    import django  # noqa
    django_version = int(django.__version__.split('.')[0])

    if not cms_present:
        return (
            'WARNING: django-cms is not installed - some of the tests will '
            'be skipped.')
    elif cms_present and django_version > 1:
        return (
            'WARNING: your django version is incompatible with django-cms. '
            'To use django-cms downgrade django to 1.11.')


def pytest_collection_modifyitems(config, items):
    try:
        import cms  # noqa
        return
    except ImportError:
        skip_cms_tests = pytest.mark.skip(
            reason='django-cms is not installed')
        for item in items:
            if 'cms' in item.keywords:
                item.add_marker(skip_cms_tests)
