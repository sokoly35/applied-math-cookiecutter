# {{cookiecutter.project_name}}
---

{{cookiecutter.description}}

## Project Organization
---

```
{%- if cookiecutter.project_size == "Small" -%}

\nPossible small project content here


{%- elif cookiecutter.project_size == "Medium" -%}

\nPossible medium project content here

{%- elif cookiecutter.project_size == "Large" -%}

\nPossible large project content here
{% endif %}
```

---