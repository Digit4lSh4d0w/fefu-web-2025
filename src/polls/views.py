from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    """Отображение корневой страницы приложения polls."""

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    @staticmethod
    def get_queryset():
        """Возвращает последние 5 опубликованных вопроса."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """Отображение страницы детализации вопроса."""

    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    """Отображение страницы результатов голосования."""

    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """Увеличивает счетчик голосов."""
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )

    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
