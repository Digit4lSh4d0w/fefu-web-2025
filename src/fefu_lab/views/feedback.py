from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fefu_lab.forms import FeedbackForm


def feedback(request: HttpRequest) -> HttpResponse:
    """Страница с формой обратной связи."""
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        return redirect("fefu_lab:index")

    return render(request, "fefu_lab/feedback.html", {"form": form})
