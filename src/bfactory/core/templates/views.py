#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

from .selectors import *
from .services import * 

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        {% for model in models -%}
        '{{model.name|lower}}s': reverse('{{model.name|lower}}s-list', request=request, format=format),
        {%- endfor %}
    })
    



{% for model in models %}

class {{model.name}}ListAPIView(ListAPIView):
    

    class OutputSerializer(serializers.Serializer):
        
        pk = serializers.CharField()
{% for field in model.fields -%}
{{ '    ' }}{{ '    ' }}{{field.name}} = {% include "helpers/field_serializer.py" %}
{%- endfor %}


    class InputSerializer(serializers.Serializer):
{% for field in model.fields if field.editable -%}
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

        {{model.name|lower}} = service.create(
            {% for field in model.fields if field.editable -%}
            {% if field.type == 'owner' %}{{field.name}}=self.request.user,
            {% else %}
            {{field.name}} = serializer.validated_data['{{field.name}}'],
            {% endif %}
            {%- endfor %}
        )

        data = self.OutputSerializer({{model.name|lower}}, many=False).data

        return Response(data, status=status.HTTP_201_CREATED)



        

class {{model.name}}APIView(APIView):
    

    class OutputSerializer(serializers.Serializer):
        
        pk = serializers.CharField()
{% for field in model.fields -%}
{{ '    ' }}{{ '    ' }}{{field.name}} = {% include "helpers/field_serializer.py" %}
{%- endfor %}


    class InputSerializer(serializers.Serializer):
{% for field in model.fields if field.editable -%}
{{ '    ' }}{{ '    ' }}{{field.name}} = {% include "helpers/field_serializer.py" %}
{%- endfor %}
        

    serializer_class = InputSerializer

    def get_queryset(self):
        return {{model.name|lower}}_list(fetched_by=self.request.user)
        


    def get(self, request, id:int):

        {{model.name|lower}} = {{model.name|lower}}_get(fetched_by=self.request.user,id=id)
        data = self.OutputSerializer({{model.name|lower}}, many=False).data
        return Response(data)

    def put(self, request, id:int):

        {{model.name|lower}} = {{model.name|lower}}_get(fetched_by=self.request.user,id=id)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        service = {{model.name}}Service(user=self.request.user)

        {{model.name|lower}} = service.update(
            {{model.name|lower}}={{model.name|lower}},
            {% for field in model.fields if field.editable -%}
            {% if field.type == 'owner' %}{{field.name}}=self.request.user,
            {% else %}
            {{field.name}} = serializer.validated_data['{{field.name}}'],
            {% endif %}
            {%- endfor %}
        )

        data = self.OutputSerializer({{model.name|lower}}, many=False).data

        return Response(data, status=status.HTTP_201_CREATED)


    def delete(self, request, id:int):

        {{model.name|lower}} = {{model.name|lower}}_get(fetched_by=self.request.user,id=id)
        
        service = {{model.name}}Service(user=self.request.user)
        
        service.delete({{model.name|lower}}={{model.name|lower}})

        return Response(status=status.HTTP_200_OK)





{% endfor %}