from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at results of question {question_id}".encode())


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}".encode())
