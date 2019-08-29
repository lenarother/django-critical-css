import requests


class CriticalException(Exception):
    pass


class PenthouseException(requests.RequestException):
    pass
