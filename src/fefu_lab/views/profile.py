from typing import final

from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


@final
class ProfileView(LoginRequiredMixin, views.View):
    template_name = "fefu_lab/profile.html"
    login_url = "fefu_lab:login"

    def get(self, request):
        return render(request, self.template_name)
