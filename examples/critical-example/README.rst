Run Example
===========

1. Run penthouse container on port 3000.
   Check whether it is running:

.. code-block:: text

    http://0.0.0.0:3000/?url=https://www.moccu.com/&css=https://www.moccu.com/static/css/styles.css

Pasting this url in your browser should generate some critical css


2. Set loopback alias:

.. code-block:: text

    sudo ifconfig lo0 alias 10.20.30.40


3. Run redis server:

.. code-block:: text

    redis-server


4. Run django-rq default worker:

.. code-block:: text

    python manage.py rqworker


5. Prepare your local django server:

.. code-block:: text

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000


6. Visit admin interface and change your page domain name into 10.20.30.40:8000.

.. code-block:: text

    http://10.20.30.40:8000/admin/sites/site/


7. Visit example page - this is a page with critical_css templatetag build in into the template.

.. code-block:: text

    http://10.20.30.40:8000/example/


8. Check in admin interface whether critical css object for /example/ url was created.

.. code-block:: text

    http://10.20.30.40:8000/admin/critical/critical/
