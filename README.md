# Installation
1. Download and install django-quran
2. Add 'quran' to INSTALLED_APPS in `settings.py`
3. Add 'url(r'^...', include('quran.urls')),' to `urls.py`
4. Run `./manage.py migrate`
5. Run `./manage.py quran_loaddata`


# Resources
- Fully verified Quranic text from [Tanzil](http://tanzil.info/wiki/Main_Page)
- Morphological data (including words, roots) from [The Quranic Arabic Corpus](http://quran.uk.net/)
- Translations from [Zekr](http://zekr.org/resources.html)