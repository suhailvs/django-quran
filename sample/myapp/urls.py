from django.conf.urls import *

urlpatterns = patterns('myapp.views',
    # Examples:
    url(r'^$', 'index', name='quran_index'),
    # aya
    url(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/$', 'aya', name='quran_aya'),
    # word_roots
    url(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/(?P<word_number>\d+)/$', 'word', name='quran_word'),

    # sura
    url(r'^(?P<sura_number>\d+)/(?P<aya_range>.+/)?$', 'sura', name='quran_sura'),

    # Parts :
    url(r'^lemma/(?P<lemma_id>\d+)/$', 'lemma', name='quran_lemma'),
    url(r'^root/(?P<root_id>\d+)/$', 'root', name='quran_root'),
    url(r'^root/$', 'root_index', name='quran_root_list'),
)