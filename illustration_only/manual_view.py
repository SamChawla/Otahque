# illustration_only/manual_view.py
# Educational illustration only: what the two shortcuts abbreviate.
from django.http import Http404, HttpRequest, HttpResponse
from django.template import loader

from events.models import Event


def event_detail_by_hand(request: HttpRequest, slug: str) -> HttpResponse:
    # get_object_or_404, unrolled:
    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("No event matches that address.")

    # render(), unrolled:
    template = loader.get_template("events/event_detail.html")
    html = template.render({"event": event}, request)
    return HttpResponse(html)
