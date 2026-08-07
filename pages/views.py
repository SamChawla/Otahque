# pages/views.py
from django.http import HttpRequest, HttpResponse
from django.utils.html import escape


def home(request: HttpRequest) -> HttpResponse:
    """The Otahque homepage."""
    html = (
        "<h1>Welcome to Otahque</h1>"
        "<p>A gathering house for your community: events, jobs, and content.</p>"
        '<p><a href="/about/">About this project</a></p>'
    )
    return HttpResponse(html)


def about(request: HttpRequest) -> HttpResponse:
    """A short description of what Otahque is."""
    html = (
        "<h1>About Otahque</h1>"
        "<p>Otahque is an open-source, community-driven platform for "
        "organizing events, posting transparent job listings, and "
        "publishing content. You are reading it during construction.</p>"
        '<p><a href="/">Back home</a></p>'
    )
    return HttpResponse(html)


def section_placeholder(request: HttpRequest, name: str) -> HttpResponse:
    """A stand-in page for a section; `name` is captured by a path converter."""
    safe_name = escape(name)
    html = (
        f"<h1>{safe_name.title()}</h1>"
        f"<p>The {safe_name} section is coming soon.</p>"
        '<p><a href="/">Back home</a></p>'
    )
    return HttpResponse(html)
