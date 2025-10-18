from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import RegistrationForm


def registration(request: HttpRequest) -> HttpResponse:
    """Страница с формой регистрации."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fefu_lab:index")
    else:
        form = RegistrationForm()
    return render(request, "fefu_lab/registration.html", {"form": form})
