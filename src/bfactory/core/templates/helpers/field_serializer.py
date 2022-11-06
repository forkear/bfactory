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
    serializers.PrimaryKeyRelatedField(many=False, read_only=True)
{% endif %}
{%- if field.type == 'datetime' -%}
    serializers.DateTimeField({% if field.default == 'now' %}auto_now=True{% endif %}{% if not field.req %}, null=True, blank=True {% endif %})
{% endif %}