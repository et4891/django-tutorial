from django.http import HttpResponse

# Uses loader to load template which will require the template variable below to be active
# There is another option which uses a shortcut called render
from django.template import loader

# This option uses render to render the view instead of using template
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') (This uses template)
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list]) (This is hard coded which is not a good idea)
    # return HttpResponse(template.render(context, request)) (This uses template)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
