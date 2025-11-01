from typing import final

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from fefu_lab.forms import CourseCreationForm, StudentEnrollmentForm
from fefu_lab.models import Course


@final
class CourseDetailView(generic.View):
    """Страница детализации информации о курсе."""

    template_name = "fefu_lab/course_details.html"

    def get(self, request, slug=None):
        course = None

        if slug:
            course = get_object_or_404(Course, slug=slug)

        form = StudentEnrollmentForm(course=course)
        return render(request, self.template_name, {"course": course, "form": form})

    def post(self, request, slug=None):
        course = None

        if slug:
            course = get_object_or_404(Course, slug=slug)

        form = StudentEnrollmentForm(request.POST, course=course)

        if form.is_valid():
            form.save()
            messages.success(request, "Студент успешно записан на курс!")
            return redirect("fefu_lab:courses_list")
        return render(request, self.template_name, {"course": course, "form": form})


def course_list(request: HttpRequest) -> HttpResponse:
    """Страница списка курсов."""
    form = CourseCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Курс успешно добавлен!")
        return redirect("fefu_lab:courses_list")

    courses = Course.objects.order_by("-created_at")
    return render(request, "fefu_lab/courses_list.html", {"courses": courses, "form": form})
