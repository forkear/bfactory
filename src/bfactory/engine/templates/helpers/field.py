{%- if field.type == 'str'  -%}
    models.CharField(max_length=80 {% if not field.req %} null=True, blank=True {% endif %})
{% endif %}
{%- if field.type == 'bool' -%}
    models.BooleanField({% if not field.req %} default=False {% endif %})
{% endif %}
{%- if field.type == 'User' -%}
    models.ForeignKey(User, on_delete=models.CASCADE)
{% endif %}
{%- if field.type == 'int' -%}
    models.PositiveIntegerField()
{% endif %}
{%- if field.type == 'fk' -%}
    models.ForeignKey("{{field.fk}}", on_delete=models.CASCADE)
{% endif %}