# events/urls.py
from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.event_list, name="list"),
    path("feed.json", views.event_feed, name="feed"),
    path("latest/", views.latest_event, name="latest"),
    path("category/<slug:slug>/", views.category_detail, name="category"),
    path("<slug:slug>/", views.event_detail, name="detail"),
]
