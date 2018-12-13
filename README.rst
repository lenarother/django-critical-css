django-critical-css
===================

.. image:: https://img.shields.io/pypi/v/django-critical-css.svg
   :target: https://pypi.org/project/django-critical-css/
   :alt: Latest Version

.. image:: https://codecov.io/gh/lenarother/django-critical-css/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lenarother/django-critical-css
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-critical-css/badge/?version=latest
   :target: https://django-critical-css.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/lenarother/django-critical-css.svg?branch=master
   :target: https://travis-ci.org/lenarother/django-critical-css


django-critical-css aims to speed up webpage rendering by saving
`critical css <http://www.phpied.com/css-and-the-critical-path/>`_ in db.


Features
--------

* critical_css templatetag to inline critical css from db.
* empty_critical_css management command.
* signal for emptying critical css on page publish action when using django-cms.


Requirements
------------

django-critical-css supports Python 3 only and requires at least Django 1.11.
Additionally, it requires requests, django-rq, and django-inline-static.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://django-critical-css.readthedocs.io>`_
* `Bug Tracker <https://github.com/lenarother/django-critical-css/issues>`_
* `Code <https://github.com/lenarother/django-critical-css/>`_
