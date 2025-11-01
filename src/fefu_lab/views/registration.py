from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import RegistrationForm, StudentRegistrationForm, TeacherRegistrationForm


def registration(request: HttpRequest) -> HttpResponse:
    """Страница с формой регистрации."""
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        role = form.cleaned_data["role"]
        if role == "student":
            return redirect("fefu_lab:registration_as_student")
        if role == "teacher":
            return redirect("fefu_lab:registration_as_teacher")
        else:
            form.add_error("role", "Выбрана некорректная роль")

    return render(request, "fefu_lab/registration.html", {"form": form})


def registration_as_student(request: HttpRequest) -> HttpResponse:
    form = StudentRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Студент успешно зарегистрирован!")
        return redirect("fefu_lab:index")
    return render(request, "fefu_lab/registration.html", {"form": form})


def registration_as_teacher(request: HttpRequest) -> HttpResponse:
    form = TeacherRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Преподаватель успешно зарегистрирован!")
        return redirect("fefu_lab:index")
    return render(request, "fefu_lab/registration.html", {"form": form})
