# illustration_only/smallest_view.py
from django.http import HttpRequest, HttpResponse


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Otahque")
