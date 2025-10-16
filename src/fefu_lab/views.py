from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from fefu_lab.forms import CourseCreationForm, FeedbackForm, StudentCreationForm
from fefu_lab.models import Course, Student


class AboutView(generic.TemplateView):
    """Страница 'о нас'."""

    template_name = "fefu_lab/about.html"


class StudentDetailView(generic.DetailView):
    """Страница детализации информации о студенте."""

    model = Student
    template_name = "fefu_lab/student_detail.html"
    context_object_name = "student"


class CourseDetailView(generic.DetailView):
    """Страница детализации информации о курсе."""

    model = Course
    template_name = "fefu_lab/course_detail.html"
    context_object_name = "course"


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

    latest_students = Student.objects.order_by("-enrollment_date")[:5]
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


def student_list(request: HttpRequest) -> HttpResponse:
    """Страница списка студентов."""
    form = StudentCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("fefu_lab:student_list")

    students = Student.objects.order_by("-enrollment_date")
    return render(request, "fefu_lab/student_list.html", {"students": students, "form": form})


def course_list(request: HttpRequest) -> HttpResponse:
    """Страница списка курсов."""
    form = CourseCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("fefu_lab:course_list")

    courses = Course.objects.order_by("-created_at")
    return render(request, "fefu_lab/course_list.html", {"courses": courses, "form": form})


def custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """Обработчик некорректных запросов."""
    return render(request, "fefu_lab/404.html", status=404)


def feedback(request: HttpRequest) -> HttpResponse:
    """Страница с формой обратной связи."""
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        return redirect("fefu_lab:index")

    return render(request, "fefu_lab/feedback.html", {"form": form})
