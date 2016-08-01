from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Get the latest 5 published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'result.html'


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
