from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import burgertime.views

urlpatterns = [
    url(r'^$', burgertime.views.index, name='index'),
]
