from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def custom_404(request: HttpRequest, _exception: Exception) -> HttpResponse:
    """Обработчик некорректных запросов."""
    return render(request, "fefu_lab/404.html", status=404)
