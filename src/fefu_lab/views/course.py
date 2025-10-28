from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from fefu_lab.forms import CourseCreationForm
from fefu_lab.models import Course


class CourseDetailView(generic.DetailView):
    """Страница детализации информации о курсе."""

    model = Course
    template_name = "fefu_lab/course_details.html"
    context_object_name = "course"


def course_list(request: HttpRequest) -> HttpResponse:
    """Страница списка курсов."""
    form = CourseCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Курс успешно добавлен!")
        return redirect("fefu_lab:courses_list")

    courses = Course.objects.order_by("-created_at")
    return render(request, "fefu_lab/courses_list.html", {"courses": courses, "form": form})
