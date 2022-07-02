from django.http.request import HttpRequest
from django.http import HttpResponse


def index(req: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "Hello, world. You're at the polls index."
    )