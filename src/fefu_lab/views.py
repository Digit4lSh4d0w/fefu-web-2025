from typing import override

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from fefu_lab.forms import CourseCreationForm, StudentCreationForm
from fefu_lab.models import Course, Student


class IndexView(generic.TemplateView):
    """Отображение корневой страницы приложения fefu_lab."""

    template_name = "fefu_lab/index.html"

    @override
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["latest_students"] = Student.objects.order_by("-enrollment_date")[:5]
        ctx["latest_courses"] = Course.objects.order_by("-created_at")[:5]
        return ctx


class AboutView(generic.TemplateView):
    template_name = "fefu_lab/about.html"


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = "fefu_lab/student_detail.html"
    context_object_name = "student"


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "fefu_lab/course_detail.html"
    context_object_name = "course"


def student_list(request: HttpRequest) -> HttpResponse:
    form = StudentCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("fefu_lab:student_list")

    students = Student.objects.order_by("-enrollment_date")[:10]
    return render(
        request,
        "fefu_lab/student_list.html",
        {"students": students, "form": form}
    )


def course_list(request: HttpRequest) -> HttpResponse:
    form = CourseCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("fefu_lab:course_list")

    courses = Course.objects.order_by("-created_at")[:10]
    return render(
        request,
        "fefu_lab/course_list.html",
        {"courses": courses, "form": form}
    )
