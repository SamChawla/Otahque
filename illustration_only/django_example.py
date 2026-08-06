# illustration_only/django_example.py
from django.views.generic import ListView
from .models import Event

class EventListView(ListView):
    model = Event
    paginate_by = 25
    # Admin, auth, ORM, migrations: all built in
