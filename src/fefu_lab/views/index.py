from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import CourseCreationForm, StudentCreationForm
from fefu_lab.models import Course, Student


def index(request: HttpRequest) -> HttpResponse:
    """Корневая страница."""
    latest_students = Student.objects.filter(is_active=True)[:5]
    latest_courses = Course.objects.order_by("-created_at")[:5]

    return render(
        request,
        "fefu_lab/index.html",
        {
            "latest_students": latest_students,
            "latest_courses": latest_courses,
        },
    )
