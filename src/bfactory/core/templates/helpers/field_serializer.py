{%- if field.type == 'str'  -%}
    serializers.CharField(max_length=128 {% if not field.req %},  allow_blank=True {% endif %})
{% endif %}
{%- if field.type == 'text'  -%}
    serializers.CharField({% if not field.req %} allow_blank=True {% endif %})
{% endif %}
{%- if field.type == 'bool' -%}
    serializers.BooleanField({% if not field.req %} default=False {% endif %})
{% endif %}
{%- if field.type == 'int' -%}
    serializers.IntegerField({% if not field.req %}required=False{% endif %})
{% endif %}
{%- if field.type == 'pint' -%}
    serializers.IntegerField(min_value=0{% if not field.req %}, required=False{% endif %})
{% endif %}
{%- if field.type == 'fk' -%}
    serializers.PrimaryKeyRelatedField(many=False, queryset={{field.fk}}.objects.all(), required={{field.req}} {% if not field.req %}, allow_null=True {% endif %})
{% endif %}
{%- if field.type == 'datetime' -%}
    serializers.DateTimeField()
{% endif %}
{%- if field.type == 'float' -%}
    serializers.DecimalField(max_digits=10, decimal_places=2)
{% endif %}
{%- if field.type == 'user' or field.type == 'owner' -%}
    serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all(), required={{field.req}} {% if not field.req %}, allow_null=True {% endif %})
{% endif %}