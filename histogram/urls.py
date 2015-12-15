# -*- coding: utf-8 -*-
from histogram.views import myview
from django.conf.urls import include, url


urlpatterns = [
    url(r'^(?P<filename>\w+\.\w+)', myview),
]