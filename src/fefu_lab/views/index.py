from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import CourseCreationForm, StudentCreationForm
from fefu_lab.models import Course, Student


def index(request: HttpRequest) -> HttpResponse:
    """Корневая страница."""
    student_form = StudentCreationForm(request.POST or None, prefix="s")
    if student_form.is_valid():
        student_form.save()
        return redirect("fefu_lab:index")

    course_form = CourseCreationForm(request.POST or None, prefix="c")
    if course_form.is_valid():
        course_form.save()
        return redirect("fefu_lab:index")

    latest_students = Student.objects.filter(is_active=True)[:5]
    latest_courses = Course.objects.order_by("-created_at")[:5]

    return render(
        request,
        "fefu_lab/index.html",
        {
            "latest_students": latest_students,
            "latest_courses": latest_courses,
            "student_form": student_form,
            "course_form": course_form,
        },
    )
