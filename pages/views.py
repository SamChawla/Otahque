# pages/views.py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from events import queries


def home(request: HttpRequest) -> HttpResponse:
    """The Otahque homepage, listing the three community pillars."""
    pillars = [
        {"name": "Events", "blurb": "Create and RSVP to community gatherings."},
        {"name": "Jobs", "blurb": "Browse transparent listings with real salaries."},
        {"name": "Content", "blurb": "Read and discuss posts from your community."},
    ]
    return render(request, "pages/home.html", {"pillars": pillars})


def about(request: HttpRequest) -> HttpResponse:
    """A short description of what Otahque is."""
    return render(request, "pages/about.html")


def section_placeholder(request: HttpRequest, name: str) -> HttpResponse:
    """A stand-in page for a section; `name` is captured by a path converter."""
    return render(request, "pages/section.html", {"name": name})


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    context = {"path": request.path, "suggestions": queries.upcoming()[:3]}
    return render(request, "404.html", context, status=404)


def server_error(request: HttpRequest) -> HttpResponse:
    return render(request, "500.html", status=500)
