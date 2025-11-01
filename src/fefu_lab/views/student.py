from typing import final

from django import views
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from fefu_lab.forms import StudentEnrollmentForm, StudentRegistrationForm
from fefu_lab.models import Student


@final
class StudentDetailView(views.View):
    """Страница детализации информации о студенте."""

    template_name = "fefu_lab/student_details.html"

    def get(self, request, pk=None):
        student = None

        if pk:
            student = get_object_or_404(Student, pk=pk)

        form = StudentEnrollmentForm(student=student)
        return render(request, self.template_name, {"student": student, "form": form})

    def post(self, request, pk=None):
        student = None

        if pk:
            student = get_object_or_404(Student, pk=pk)

        form = StudentEnrollmentForm(request.POST, student=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Студент успешно записан на курс!")
            return redirect("fefu_lab:students_list")
        return render(request, self.template_name, {"student": student, "form": form})


def student_list(request: HttpRequest) -> HttpResponse:
    """Страница списка студентов."""
    form = StudentRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Студент успешно добавлен!")
        return redirect("fefu_lab:students_list")

    students = Student.objects.filter(is_active=True)[:5]
    return render(request, "fefu_lab/students_list.html", {"students": students, "form": form})
