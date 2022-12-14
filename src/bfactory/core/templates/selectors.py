#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from  django.db import models
from  django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime
from typing import Iterable

{% for model in models %}
from .models import {{model.name}}
{% endfor %}

{% for model in models %}
# {{model.name}}

def {{model.name|lower}}_list(*, fetched_by: User) -> Iterable[{{model.name}}]:
    
    return {{model.name}}.objects.all()

def {{model.name|lower}}_get(*, fetched_by: User, id: int) -> {{model.name}}:
    
    return {{model.name}}.objects.get(id=id)
{% endfor %}