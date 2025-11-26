from typing import final

from django import views
from django.contrib import messages
from django.shortcuts import redirect, render

from fefu_lab.forms import StudentEnrollmentForm
from fefu_lab.models import Course, StudentProfile


@final
class IndexView(views.View):
    template_name = "fefu_lab/index.html"

    def get(self, request):
        latest_students = StudentProfile.objects.filter(is_active=True)[:5]
        latest_courses = Course.objects.filter(is_active=True).order_by("-created_at")[
            :5
        ]
        form = StudentEnrollmentForm()

        return render(
            request,
            self.template_name,
            {
                "latest_students": latest_students,
                "latest_courses": latest_courses,
                "studentEnrollmentForm": form,
            },
        )

    def post(self, request):
        form = StudentEnrollmentForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Студент успешно записан на курс!")
            return redirect("fefu_lab:index")

        latest_students = StudentProfile.objects.filter(is_active=True)[:5]
        latest_courses = Course.objects.filter(is_active=True).order_by("-created_at")[
            :5
        ]

        return render(
            request,
            self.template_name,
            {
                "latest_students": latest_students,
                "latest_courses": latest_courses,
                "studentEnrollmentForm": form,
            },
        )
