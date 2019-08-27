Installation
============

* Install with pip::

    pip install django-critical-css


* Your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # ...

        'django_rq',
        'inline_static',

        'critical',
    )

* Settings::

    You can run an instance of `penthouse service <https://github.com/moccu/penthouse-service>`_ and add its url to settings.
    PENTHOUSE_URL = 'http://penthouse:3000/'

    Or you can configure your own function to critical css calculation.
    This function needs to accept two args - target url and target css path.
    CRITICAL_CSS_BACKEND = 'function.calculating.critical.css'

* It is possible to use critical with django-cms. If you decide to do so refer to
  `cms installation instructions <http://docs.django-cms.org/en/latest/introduction/install.html>`_.
