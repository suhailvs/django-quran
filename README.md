
# django-quran2

Quran app for Django.

## How to Package  

Refer to the Django documentation: [Reusable Apps Guide](https://docs.djangoproject.com/en/5.1/intro/reusable-apps/)

```bash
pip install build
pip install twine
rm -rf dist/
python -m build
twine upload dist/*
```

## Quick Start


Install from pip: `pip install djangoquran2`

1. Add `djangoquran2` to your INSTALLED_APPS setting like this::

    `INSTALLED_APPS = [...,"djangoquran2",]`

2. Include the djangoquran2 URLconf in your project `urls.py` like this::

    `path("quran/", include("djangoquran2.urls")),`

3. Run `python manage.py migrate` to create the models.

4. Run `python manage.py loadquran` to load datas.

5. Visit the ``/quran/`` URL.