============
django-quran
============

Quran app for django.

how to packaging: https://docs.djangoproject.com/en/5.1/intro/reusable-apps/


Quick start
-----------

Install from pip: `pip install djangoquran`

1. Add "djangoquran" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "djangoquran",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("quran/", include("djangoquran.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Run ``python manage.py loadquran`` to load datas.

5. Visit the ``/quran/`` URL.