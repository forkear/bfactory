#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .selectors import *
from .services import * 

{% for model in models %}
class {{model.name}}ListApi(APIView):
    

    class OutputSerializer(serializers.Serializer):
        
        pk = serializers.CharField()
{% for field in model.fields -%}
{{ '    ' }}{{ '    ' }}{{field.name}} = {% include "helpers/field_serializer.py" %}
{%- endfor %}


    class InputSerializer(serializers.Serializer):
{% for field in model.fields -%}
{{ '    ' }}{{ '    ' }}{{field.name}} = {% include "helpers/field_serializer.py" %}
{%- endfor %}
        

    queryset = {{model.name|lower}}_list(fetched_by=None)
    serializer_class = InputSerializer

    def get(self, request):

        {{model.name|lower}}s = {{model.name|lower}}_list(fetched_by=self.request.user)
        data = self.OutputSerializer({{model.name|lower}}s, many=True).data
        return Response(data)


    def post(self, request):

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        service = {{model.name}}Service(user=self.request.user)

        service.create(
            {% for field in model.fields -%}
            {% if field.type == 'User' %}{{field.name}}=self.request.user{% else %}{{field.name}} = serializer.validated_data['{{field.name}}'],
            {% endif %}
            {%- endfor %}
        )

        return Response(status=status.HTTP_201_CREATED)




{% endfor %}