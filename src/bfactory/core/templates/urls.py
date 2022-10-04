#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from rest_framework import routers
from django.urls import path, include
from django.conf import settings

router = routers.SimpleRouter()
#router.register(r'users', UserViewSet)
#router.register(r'accounts', AccountViewSet)

from .views import *

urlpatterns = [
    {% for model in models %}
    path('{{model.name|lower}}s/', {{model.name}}ListApi.as_view()){%- if not loop.last %},{% endif %}
    {% endfor %}
]

urlpatterns += router.urls