# Installation

## Run the sample project

1. Download(or clone) `django-quran`
2. Run the sample(`migrate`,`loaddata` and `runserver`)

ie:

```shell
cd sample
python3 -m venv env
source env/bin/activate
pip install django
pip install -e ../
./manage.py migrate
./manage.py quran_loaddata
./manage.py runserver
```

## On a custom project

1. Download and install `django-quran`
2. Add `'quran'` to `INSTALLED_APPS` in `settings.py`
3. Run `./manage.py migrate` and `./manage.py quran_loaddata`
4. Run the server `./manage.py runserver`


# Resources

- Fully verified Quranic text from [Tanzil](http://tanzil.info/wiki/Main_Page)
- Morphological data (including words, roots) from [The Quranic Arabic Corpus](http://quran.uk.net/)
- Translations from [Zekr](http://zekr.org/resources.html)