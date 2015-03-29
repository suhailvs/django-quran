from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.index', name='index'),
    url(r'^q/', include('quran.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
