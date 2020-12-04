from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from .models import Quiz, Question_audio, Answer
from django.db.models import F


class QuizHomeClass(ListView):
    model = Quiz
    template_name = "blog/index.html"
    context_object_name = 'quizes'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Викторины'
        return(context)



def QuizHome(request: HttpRequest):
    return render(request, 'blog/index.html')

class GetQuiz(DetailView):
    model = Quiz
    template_name = "blog/quiz_item.html"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        act_Quiz = Quiz.objects.get(slug=self.kwargs['slug'])
        act_Quiz = self.object
        self.object.views_number = F('views_number') + 1
        self.object.save()
        self.object.refresh_from_db()
        # context['title'] = "Викторина"
        return(context)


