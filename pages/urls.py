# pages/urls.py
from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("section/<str:name>/", views.section_placeholder, name="section"),
]
