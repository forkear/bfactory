#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

{% for model in models %}
class {{model.name}}(models.Model):

{% for field in model.fields -%}
{{ '    ' }}{{field.name}} = {% include "helpers/field.py" %}
{%- endfor %}

    def __str__(self):
        return f"{{model.name}} - {self.id}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def clean(self):
        #TODO: validation here
        #raise ValidationError
        pass 
    

{% endfor %}
