# {{cookiecutter.project_name}}
---

{{cookiecutter.description}}

## Project Organization
---

```
{%+ if cookiecutter.project_size == "Small" -%}
Possible small project content here


{%+ elif cookiecutter.project_size == "Medium" -%}
Possible medium project content here

{%+ elif cookiecutter.project_size == "Large" -%}
Possible large project content here
{% endif %}
```

---