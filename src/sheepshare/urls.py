from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'sheepshare.views.home', name='home'),
	url(r'^upload$', 'sheepshare.views.upload', name='upload'),
)
