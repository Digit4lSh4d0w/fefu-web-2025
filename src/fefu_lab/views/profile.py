from typing import final

from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


@final
class ProfileView(LoginRequiredMixin, views.View):
    login_url = "fefu_lab:login"

    def get(self, request):
        return render(request, "fefu_lab/profile.html")

    def get_template_name(self):
        return "fefu_lab/profile/student.html"
