from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Question


# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_questions])
    return render(request, 'index.html',
                  {'latest_questions': latest_questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        selected = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice, or your choice '
                             'was invalid.'
        })
    else:
        selected.votes += 1
        selected.save()

        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))
