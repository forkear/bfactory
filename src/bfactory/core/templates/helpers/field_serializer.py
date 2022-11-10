{%- if field.type == 'str'  -%}
    serializers.CharField(max_length=128 {% if not field.req %},  allow_blank=True {% endif %})
{% endif %}
{%- if field.type == 'text'  -%}
    serializers.CharField({% if not field.req %} allow_blank=True {% endif %})
{% endif %}
{%- if field.type == 'bool' -%}
    serializers.BooleanField({% if not field.req %} default=False {% endif %})
{% endif %}
{%- if field.type == 'user' or field.type == 'owner' -%}
    models.ForeignKey(User, on_delete=models.CASCADE{% if not field.req %}, null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'int' -%}
    models.PositiveIntegerField({% if not field.req %}null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'fk' -%}
    serializers.PrimaryKeyRelatedField(many=False, queryset={{field.fk}}.objects.all(), required={{field.req}} {% if not field.req %}, allow_null=True {% endif %})
{% endif %}
{%- if field.type == 'datetime' -%}
    serializers.DateTimeField()
{% endif %}