Usage
=====

Prerequisites
-------------

To perform its function, django-critical-css requires:

* service for critical css calculation available
  (e.g. `penthouse-service <https://github.com/moccu/penthouse-service>`_).
* redis worker available.


Templatetag for inlining critical css
-------------------------------------

django-critical-css provides the `critical_css` templatetag to inline critical css
from the database into your template using ``templates/critical/critical.html``.

.. code-block:: text

    {% load critical_tags %}

    {% critical_css 'your/css/styles_path.css' %}

If page does not have any critical css saved in the database yet or the css path of the saved
 critical-cms-object is different than the argument of `critical_css` the tag will return a normal stylesheet link-tag.
The css path will be modified as when using the django `static` templatetag, e.g.:

.. code-block:: text

    <link rel="stylesheet" type="text/css" href="/your_static_url/your/css/styles_path.css" />

Additionally, the templatetag will asynchronously trigger the calculation of critical css.


Object for saving critical css
------------------------------

Critical css is saved into the database together with the page url, the url of the css file,
and the date of last modification.


Critical css calculation
------------------------

The calculation of the critical css itself is not within the scope of this library.
You have to use an external service that does this job.
The default backend is `penthouse-service <https://github.com/moccu/penthouse-service>`_.
To use it run an instance of the service and provide the url in settings:

.. code-block:: text

    PENTHOUSE_URL = 'http://your_penthouse:3000/'

You can provide an `additional configuration <https://github.com/moccu/penthouse-service#options>`_
to penthouse-service.

.. code-block:: text

  PENTHOUSE_CONFIG = {
      'width': '720',
      'propertiesToRemove': [
          '(.*)animation(.*)',
          '(.*)transition(.*)',
      ]
  }

Alternatively, you can define your custom function,
which takes url and css path as arguments and returns critical css as string.

.. code-block:: text

    CRITICAL_CSS_BACKEND = 'function.calculating.critical.css'


Management command for emptying critical css
--------------------------------------------

django-critical-css provides a management command to remove all critical-css-objects
saved in the database. It will cause recalculation of critical css for each page
on the first request.

.. code-block:: text

    python manage.py empty_critical_css


Additional settings
-------------------

* By setting ``CRITICAL_CSS_ACTIVE`` to `False` you can deactivate css calculation
  for your dev environment. By default critical css calculation is set to active.
* By setting ``CRITICAL_CSS_IGNORE_QUERY_STRING`` to `False` you can ignore query string
  in the url. Then both urls `/?p=1`and `/?p=2` will be treated as one `/` and only one database
  object will be created.

Usage with django-cms
---------------------

It is possible to use django-critical-css together with the django-cms library.
If django-cms is installed, a signal for deleting critical css upon publication of a page
will be activated. This way, if the page changes, the critical css
is recalculated and no obsolete content is shown. In draft mode, critical css
is not active - the draft pages are always rendered through the traditional path.
