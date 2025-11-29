from typing import final

from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from fefu_lab.models import Course, get_user_role


@final
class ProfileView(LoginRequiredMixin, views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        role = get_user_role(request.user)
        if role == "student":
            courses = (
                Course.objects.filter(
                    enrollment__student=request.user.studentprofile,
                    enrollment__is_active=True,
                    is_active=True,
                )
                .order_by("-created_at")
                .distinct()
            )
            return render(
                request, "fefu_lab/profile/student.html", {"courses": courses}
            )
        elif role == "teacher":
            courses = (
                Course.objects.filter(
                    teacher=request.user.teacherprofile,
                    is_active=True,
                )
                .order_by("-created_at")
                .distinct()
            )
            return render(
                request, "fefu_lab/profile/teacher.html", {"courses": courses}
            )
        else:
            return render(request, "fefu_lab/profile/default.html")
