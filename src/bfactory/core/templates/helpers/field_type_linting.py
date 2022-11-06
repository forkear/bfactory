{%- if field.type == 'str' or field.type == 'text'  -%}str{% endif %}
{%- if field.type == 'bool' -%}bool{% endif %}
{%- if field.type == 'user' or field.type == 'owner' -%}User{% endif %}
{%- if field.type == 'int' -%}int{% endif %}
{%- if field.type == 'fk' -%}{{field.fk}}{% endif %}
{%- if field.type == 'datetime' -%}datetime{% endif %}