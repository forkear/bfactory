#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from rest_framework import routers
from django.urls import path, include
from django.conf import settings

router = routers.SimpleRouter()

from .views import *

urlpatterns = [
    path('', api_root, name='api_root'),
    {% for model in models %}
    path('{{model.name|lower}}s/', {{model.name}}ListAPIView.as_view(), name='{{model.name|lower}}s-list'),
    path('{{model.name|lower}}s/<int:id>/', {{model.name}}APIView.as_view()){%- if not loop.last %},{% endif %}
    
    {% endfor %}
]

urlpatterns += router.urls