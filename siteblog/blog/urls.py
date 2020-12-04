from django.urls import path

from  .views import QuizHomeClass, GetQuiz

urlpatterns = [
    path("", QuizHomeClass.as_view(), name="QuizList"),
    path("quiz/<str:slug>/", GetQuiz.as_view(), name="QuizItem")
]
