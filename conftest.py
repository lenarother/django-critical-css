import pytest


def pytest_report_header(config):
    try:
        import cms  # noqa
        return
    except ImportError:
        return (
            'WARNING: django-cms is not installed - some of the tests will '
            'be skipped.')


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
