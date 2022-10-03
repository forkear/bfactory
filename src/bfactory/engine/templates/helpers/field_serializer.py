{%- if field.type == 'str'  -%}
    serializers.CharField(max_length=80 {% if not field.req %} null=True, blank=True {% endif %})
{% endif %}
{%- if field.type == 'bool' -%}
    serializers.BooleanField({% if not field.req %} default=False {% endif %})
{% endif %}
{%- if field.type == 'User' -%}
    serializers.PrimaryKeyRelatedField(many=False, read_only=True)
{% endif %}
{%- if field.type == 'int' -%}
    serializers.PositiveIntegerField()
{% endif %}
{%- if field.type == 'fk' -%}
    serializers.PrimaryKeyRelatedField(many=False, read_only=True)
{% endif %}