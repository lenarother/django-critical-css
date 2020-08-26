import logging

import requests
from django.conf import settings

from .exceptions import PenthouseException
from .utils import complete_url

logger = logging.getLogger(__name__)


class PenthouseApi(object):
    @property
    def base_url(self):
        if not getattr(settings, 'PENTHOUSE_URL', None):
            raise PenthouseException(
                'Penthouse api inproperly configurred: '
                'set PENTHOUSE_URL in your settings file.'
            )
        return settings.PENTHOUSE_URL

    def get_params(self, url, css_path):
        params = {'url': complete_url(url), 'css': complete_url(css_path)}
        params.update(getattr(settings, 'PENTHOUSE_CONFIG', {}))
        return params

    def request_critical_css(self, target_url, target_css):
        params = self.get_params(target_url, target_css)

        logger.info(
            'Api: Requesting critical css from {0}, with args {1}'.format(
                self.base_url, str(params)
            )
        )

        try:
            response = requests.get(self.base_url, params)
            logger.info('Api: Critical call: {0}'.format(response.url))
            response.raise_for_status()
        except requests.RequestException as exc:
            raise PenthouseException(exc, response=exc.response)

        if response.status_code != 200:
            raise PenthouseException(
                'Invalid status code from penthouse, ' 'params: {0}'.format(params)
            )

        return response

    def get_critical_css(self, target_url, target_css):
        response = self.request_critical_css(target_url, target_css)

        if len(response.text) < 3 or response.text[:3].isdigit():
            raise PenthouseException(
                'Invalid penthouse response ({0}): '
                'url - {1}, css - {2}'.format(response.text, target_url, target_css)
            )

        return response.text


def calculate_critical_css(url, css):
    api = PenthouseApi()
    return api.get_critical_css(url, css)
