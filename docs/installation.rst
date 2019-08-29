Installation
============

* Install with pip::

.. code-block:: text

    pip install django-critical-css

* Your ``INSTALLED_APPS`` setting::

.. code-block:: text

    INSTALLED_APPS = (
        # ...

        'django_rq',
        'inline_static',

        'critical',
    )

* Settings::

You can run an instance of `penthouse service <https://github.com/moccu/penthouse-service>`_ and add its url to settings.

.. code-block:: text

    PENTHOUSE_URL = 'http://penthouse:3000/'

Alternatively, you can define your custom function,
which takes url and css path as arguments and returns critical css as string.

.. code-block:: text

    CRITICAL_CSS_BACKEND = 'function.calculating.critical.css'

* It is possible to use critical with django-cms. If you decide to do so refer to
  `cms installation instructions <http://docs.django-cms.org/en/latest/introduction/install.html>`_.
