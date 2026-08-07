# illustration_only/minimal_template_engine.py
# Educational illustration only. This is the IDEA behind a template engine,
# not Django's real implementation (no escaping, no tags, no inheritance).

import re

TOKEN = re.compile(r"\{\{\s*(\w+)\s*\}\}")


def render_template(source: str, context: dict[str, str]) -> str:
    """Replace every {{ name }} with context[name]."""
    return TOKEN.sub(lambda m: str(context.get(m.group(1), "")), source)


if __name__ == "__main__":
    template = "<h1>Welcome, {{ name }}</h1><p>{{ tagline }}</p>"
    html = render_template(template, {"name": "Otahque", "tagline": "Gather here."})
    print(html)
