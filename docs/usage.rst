Usage
=====

Prerequisites
-------------

django-critical-css to perform its function requires:

* `penthouse <https://www.npmjs.com/package/penthouse/>`_ service available.
* redis worker available.


Templatetag for inlining critical css
-------------------------------------

django-critical-css provides the critical_css templatetag to inline critical css
from database into your template using ``templates/critical/critical.html``.

.. code-block:: text

    {% load critical_tags %}

      {% critical_css 'your/css/styles_path.css' %}

If page does not have critical css saved in the database yet or css path of saved
critical-cms-object is different than input one the tag will return a normal css link.
Css path will be modified as with using django static templatetag. E.g.:

.. code-block:: text

    <link rel="stylesheet" type="text/css" href="/your_static_url/your/css/styles_path.css" />

Additionally, the templatetag will asynchronously trigger calculation of critical css.


Object for saving critical css
------------------------------

Critical css is saved into database together with page url, url to css file,
and date of last modification. The critical css is calculated through
penthouse service. It is required to provide ``PENTHOUSE_HOST`` in settings.


Management command for emptying critical css
--------------------------------------------

django-critical-css provides a managemant command to remove all critical-css-objects
saved in database. It will cause recalculation of critical css for each page
on the first request.

.. code-block:: text

    python manage.py empty_critical_css


Additional settings
-------------------

* By setting ``CRITICAL_CSS_ACTIVE`` to False you can deactivate css calculation
  for your dev environment. By default critical css calculation is always active.
* ``PENTHOUSE_CONFIG`` is a dict of additional configuration options that will
  be send to penthouse service along with page url and css path. See available
	options `here <http://www.phpied.com/css-and-the-critical-path/>`_. By default
  the dict is empty.


Usage with django-cms
---------------------

It is possible to use django-critical-css together with django-cms library.
If django-cms is installed a signal for delating page critical css on page
publish action will be activated. This way, if page changes the critical css
is recalculated and no obsolete content is shown. In draft modus critical css
is not active - the draft pages always render through traditional path.
