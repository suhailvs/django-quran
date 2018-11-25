from django.conf.urls import *
from . import views
urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='quran_index'),
    url(r'^(?P<sura_number>\d+)/$', views.sura, name='quran_sura'),

    # Parts : 
	url(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/$', views.aya, name='quran_aya'),
    url(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/(?P<word_number>\d+)/$', views.word, name='quran_word'),
    url(r'^lemma/(?P<lemma_id>\d+)/$', views.lemma, name='quran_lemma'),
    url(r'^root/(?P<root_id>\d+)/$', views.root, name='quran_root'),
    url(r'^root/$', views.root_index, name='quran_root_list'),
]