{%- if field.type == 'str'  -%}
    models.CharField(max_length=128 {% if not field.req %}, null=True, blank=True {% endif %})
{% endif %}
{%- if field.type == 'text'  -%}
    models.TextField({% if not field.req %} null=True, blank=True {% endif %})
{% endif %}
{%- if field.type == 'bool' -%}
    models.BooleanField({% if not field.req %} default=False {% endif %})
{% endif %}
{%- if field.type == 'user' or field.type == 'owner' -%}
    models.ForeignKey(User, related_name="{{model.name|lower}}_{{field.name|lower}}_user", on_delete=models.CASCADE{% if not field.req %}, null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'int' -%}
    models.IntegerField({% if not field.req %}null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'decimal' -%}
    models.DecimalField(max_digits=10, decimal_places=2{% if not field.req %}, null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'pint' -%}
    models.PositiveIntegerField({% if not field.req %}null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'fk' -%}
    models.ForeignKey("{{field.fk}}", related_name="{{model.name|lower}}_{{field.name|lower}}_{{field.fk|lower}}", on_delete=models.CASCADE{% if not field.req %},null=True, blank=True{% endif %})
{% endif %}
{%- if field.type == 'datetime' -%}
    models.DateTimeField({% if field.default == 'now' %}auto_now=True{% endif %}{% if not field.req %}, null=True, blank=True {% endif %})
{% endif %}
