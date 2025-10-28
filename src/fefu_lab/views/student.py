from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from fefu_lab.forms import StudentCreationForm
from fefu_lab.models import Student


class StudentDetailView(generic.DetailView):
    """Страница детализации информации о студенте."""

    model = Student
    template_name = "fefu_lab/student_detail.html"
    context_object_name = "student"


def student_list(request: HttpRequest) -> HttpResponse:
    """Страница списка студентов."""
    form = StudentCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("fefu_lab:student_list")

    students = Student.objects.filter(is_active=True)[:5]
    return render(request, "fefu_lab/student_list.html", {"students": students, "form": form})
