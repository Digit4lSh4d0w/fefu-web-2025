from typing import final

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from fefu_lab.forms import CourseCreationForm, StudentEnrollmentForm
from fefu_lab.models import Course, Enrollment, get_user_profile, get_user_role


@final
class CourseDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.View):
    """Страница детализации информации о курсе."""

    template_name = "fefu_lab/course/details.html"
    permission_required = "fefu_lab.view_course"

    def get(self, request, slug=None):
        course = get_object_or_404(Course, slug=slug, is_active=True)
        if not has_course_access(request.user, course):
            messages.error(request, "У вас нет доступа к этому курсу!")
            return redirect("fefu_lab:courses_list")

        student = None
        if get_user_role(request.user) == "student":
            student = get_user_profile(request.user)

        form = StudentEnrollmentForm(course=course, student=student)
        return render(request, self.template_name, {"course": course, "form": form})

    def post(self, request, slug=None):
        course = get_object_or_404(Course, slug=slug, is_active=True)
        if not has_course_access(request.user, course):
            messages.error(request, "У вас нет доступа к этому курсу!")
            return redirect("fefu_lab:courses_list")

        role = get_user_role(request.user)
        if role != "student":
            messages.error(request, "Только студенты могут записываться на курс!")
            return redirect("fefu_lab:courses_list")

        form = StudentEnrollmentForm(
            request.POST,
            course=course,
            student=get_user_profile(request.user),
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно записаны на курс!")
            return redirect("fefu_lab:courses_list")
        return render(request, self.template_name, {"course": course, "form": form})


@login_required
@permission_required("fefu_lab.add_course")
def course_create(request: HttpRequest) -> HttpResponse:
    """Страница создания курса."""
    form = CourseCreationForm(request.POST or None)
    if form.is_valid():
        course = form.save(commit=False)
        course.teacher = request.user.teacherprofile
        course.save()
        messages.success(request, "Курс успешно добавлен!")
        return redirect("fefu_lab:course_create")

    return render(request, "fefu_lab/course/create.html", {"form": form})


@login_required
@permission_required("fefu_lab.view_course")
def course_list(request: HttpRequest) -> HttpResponse:
    """Страница списка курсов."""

    role = get_user_role(request.user)
    courses = Course.objects.filter(is_active=True).order_by("-created_at")

    if role == "teacher":
        courses = courses.filter(teacher=request.user.teacherprofile)
    elif role == "student":
        courses = courses.filter(
            enrollment__student=request.user.studentprofile,
            enrollment__is_active=True,
        ).distinct()
    else:
        courses = courses.none()

    return render(request, "fefu_lab/course/list.html", {"courses": courses})


@login_required
@permission_required("fefu_lab.change_course")
def course_update(request: HttpRequest, slug: str) -> HttpResponse:
    """Редактирование своего курса."""
    course = get_object_or_404(Course, slug=slug, is_active=True)
    if course.teacher != request.user.teacherprofile:
        messages.error(request, "Вы можете редактировать только свои курсы!")
        return redirect("fefu_lab:courses_list")

    form = CourseCreationForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Курс успешно обновлен!")
        return redirect("fefu_lab:courses_list")

    else:
        form = CourseCreationForm(instance=course)

    return render(request, "fefu_lab/course/create.html", {"form": form})


def has_course_access(user, course) -> bool:
    """Проверяет доступ к курсу."""
    role = get_user_role(user)
    if role == "student":
        return Enrollment.objects.filter(
            student=user.studentprofile,
            course=course,
            is_active=True,
        ).exists()
    elif role == "teacher":
        return course.teacher == user.teacherprofile
    return False
