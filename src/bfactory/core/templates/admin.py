#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import *


{% for model in models %}
class {{model.name}}Admin(admin.ModelAdmin):

    list_display = ({% for field in model.fields %}'{{field.name}}',{%endfor%})
    search_fields = ({% for field in model.fields %}{% if field.type == 'str' %}'{{field.name}}',{%endif%}{%endfor%})
    list_filter = ({% for field in model.fields %}{% if field.type == 'bool' %}'{{field.name}}',{%endif%}{%endfor%})
    
admin.site.register({{model.name}}, {{model.name}}Admin)

{% endfor %}

