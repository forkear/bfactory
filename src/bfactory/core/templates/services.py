#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from datetime import datetime

{% for model in models %}from .models import {{model.name}}
{% endfor %}

{% for model in models %}
class {{model.name}}Service:
    
    def __init__(self, user: User = None):
        self._user = user
    
    @transaction.atomic
    def create(
        self,{%- for field in model.fields if field.editable  %}
        {{field.name}}: {%- include "helpers/field_type_linting.py" -%},{%endfor -%}
    ) -> {{model.name}}:

        {{model.name|lower}} = {{model.name}}({% for field in model.fields if field.editable %}
                {{field.name}}={{field.name}},
                {%- endfor%}
        )

        {{model.name|lower}}.full_clean()
        {{model.name|lower}}.save()

        return {{model.name|lower}}

    @transaction.atomic
    def update(
        self,
        {{model.name|lower}}: {{model.name}}, {% for field in model.fields if field.editable %}
        {{field.name}}: {% include "helpers/field_type_linting.py" %},{%endfor%}
    ) -> {{model.name}}:
        {% for field in model.fields if field.editable %}
        {{model.name|lower}}.{{field.name}}={{field.name}}{%endfor%}
        
        {{model.name|lower}}.full_clean()
        {{model.name|lower}}.save()
        return {{model.name|lower}}


    @transaction.atomic
    def delete(
        self,
        {{model.name|lower}}: {{model.name}}   
    ) -> None:

        {{model.name|lower}}.delete()

        return
        
    
    
{%endfor %}