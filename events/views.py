# events/views.py
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . import queries
from .models import Category


def event_list(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    if query:
        events = queries.search(query)
        heading = f'Results for "{query}"'
    else:
        events = queries.upcoming()
        heading = "Upcoming events"
    events = events.select_related("category")
    context = {"events": events, "heading": heading, "query": query}
    return render(request, "events/event_list.html", context)


def event_detail(request: HttpRequest, slug: str) -> HttpResponse:
    event = get_object_or_404(
        queries.published().select_related("category", "organizer").prefetch_related("tags"),
        slug=slug,
    )
    return render(request, "events/event_detail.html", {"event": event})


def category_detail(request: HttpRequest, slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=slug)
    events = queries.by_category(slug).select_related("category")
    context = {"events": events, "heading": category.name, "query": ""}
    return render(request, "events/event_list.html", context)


def latest_event(request: HttpRequest) -> HttpResponse:
    event = queries.upcoming().first()
    if event is None:
        raise Http404("No upcoming events yet.")
    return redirect("events:detail", slug=event.slug)


def event_feed(request: HttpRequest) -> JsonResponse:
    events = [
        {
            "title": event.title,
            "starts_at": event.starts_at.isoformat(),
            "url": reverse("events:detail", args=[event.slug]),
        }
        for event in queries.upcoming()
    ]
    return JsonResponse({"count": len(events), "events": events})
