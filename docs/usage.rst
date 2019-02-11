Usage
=====

Prerequisites
-------------

To perform its function, django-critical-css requires:

* `penthouse <https://www.npmjs.com/package/penthouse/>`_ service available.
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
and the date of last modification. The critical css is calculated through
a penthouse service. You need to provide ``PENTHOUSE_HOST`` in settings.


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
  for your dev environment. By default critical css calculation is always active.
* ``PENTHOUSE_CONFIG`` is a dict with additional configuration options that will
  be sent to the penthouse service along with the page url and css path. See available
 	options `here <https://github.com/moccu/penthouse-service#options>`_. By default
  the dict is empty.


Usage with django-cms
---------------------

It is possible to use django-critical-css together with the django-cms library.
If django-cms is installed, a signal for deleting critical css upon publication of a page
will be activated. This way, if the page changes, the critical css
is recalculated and no obsolete content is shown. In draft mode, critical css
is not active - the draft pages are always rendered through the traditional path.
