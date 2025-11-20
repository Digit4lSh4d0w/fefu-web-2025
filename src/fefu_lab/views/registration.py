from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import RegistrationForm
from fefu_lab.models import StudentProfile, TeacherProfile


def registration(request: HttpRequest) -> HttpResponse:
    """Страница с формой регистрации."""
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()

        role = form.cleaned_data["role"]
        if role == "student":
            StudentProfile.objects.create(
                user=user,
                birthday=form.cleaned_data["birthday"],
                faculty=form.cleaned_data["faculty"],
            )
            students_group, _ = Group.objects.get_or_create(name="Студенты")
            user.groups.add(students_group)

            messages.success(request, f"Аккаунт {user.username} успешно создан!")
            return redirect("fefu_lab:index")

        elif role == "teacher":
            TeacherProfile.objects.create(
                user=user,
                birthday=form.cleaned_data["birthday"],
            )
            teachers_group, _ = Group.objects.get_or_create(name="Преподаватели")

            permission = Permission.objects.get(codename="add_course")
            teachers_group.permissions.add(permission)

            user.groups.add(teachers_group)

            messages.success(request, f"Аккаунт {user.username} успешно создан!")
            return redirect("fefu_lab:index")

        else:
            form.add_error("role", "Выбрана некорректная роль")
            return render(request, "fefu_lab/auth/registration.html", {"form": form})

    return render(request, "fefu_lab/auth/registration.html", {"form": form})
