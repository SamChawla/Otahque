# events/queries.py
"""Query helpers for the events app; Chapter 37 graduates these into a custom manager."""
from django.db.models import Q, QuerySet
from django.utils import timezone

from .models import Event


def published() -> QuerySet[Event]:
    """Everything a visitor is allowed to see."""
    return Event.objects.filter(status=Event.Status.PUBLISHED)


def upcoming() -> QuerySet[Event]:
    """Published events that have not started yet, soonest first."""
    return published().filter(starts_at__gte=timezone.now()).order_by("starts_at")


def by_location(location: str) -> QuerySet[Event]:
    """Published events at a venue, case-insensitive."""
    return published().filter(location__iexact=location)


def search(term: str) -> QuerySet[Event]:
    """Published events mentioning the term in title or description."""
    return published().filter(
        Q(title__icontains=term) | Q(description__icontains=term)
    )
