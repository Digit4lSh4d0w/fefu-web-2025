from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import RegistrationForm


def registration(request: HttpRequest) -> HttpResponse:
    """Страница с формой регистрации."""
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Регистрация успешно завершена!")
        return redirect("fefu_lab:index")

    return render(request, "fefu_lab/registration.html", {"form": form})
