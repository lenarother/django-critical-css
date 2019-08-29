from django.conf import settings
from django.utils.module_loading import import_string


def calculate_critical_css(target_url, css_pyth):
    calculate_function_str = getattr(
        settings, 'CRITICAL_CSS_BACKEND', 'critical.api.calculate_critical_css'
    )
    calculate_function = import_string(calculate_function_str)
    return calculate_function(target_url, css_pyth)
