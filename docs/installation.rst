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

* Required settings::

    PENTHOUSE_HOST = ...  # host of your critical path css generator service

* It is possible to use critical with django-cms. If you decide to do so refer to
  `cms installation instructions <http://docs.django-cms.org/en/latest/introduction/install.html>`_.
