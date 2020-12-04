
from django.db import models
from django.urls import reverse

class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название викторины')
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    views_number = models.IntegerField(default=0, verbose_name="кол просмотров")
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField(verbose_name="Показывать после")
    question1 = models.ForeignKey("Question_audio", verbose_name="Вопрос 1", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes1")
    question2 = models.ForeignKey("Question_audio", verbose_name="Вопрос 2", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes2")
    question3 = models.ForeignKey("Question_audio", verbose_name="Вопрос 3", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes3")
    question4 = models.ForeignKey("Question_audio", verbose_name="Вопрос 4", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes4")
    question5 = models.ForeignKey("Question_audio", verbose_name="Вопрос 5", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes5")
    question6 = models.ForeignKey("Question_audio", verbose_name="Вопрос 6", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes6")
    question7 = models.ForeignKey("Question_audio", verbose_name="Вопрос 7", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes7")
    question8 = models.ForeignKey("Question_audio", verbose_name="Вопрос 8", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes8")
    question9 = models.ForeignKey("Question_audio", verbose_name="Вопрос 9", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes9")
    questio10 = models.ForeignKey("Question_audio", verbose_name="Вопрос 10", on_delete=models.PROTECT, blank=True,
                                  null=True, related_name="quizes10")

    def __str__(self):
        return "Викторина: " + self.title

    class Meta:
        verbose_name = "Викторина"
        verbose_name_plural = "Викторины"
        ordering = ["created_at"]

    def get_absolut_url(self):
        return reverse("QuizItem", kwargs={"slug": self.slug})

class Question_audio(models.Model):
    number = models.IntegerField(verbose_name="Порядковый номер")
    comment = models.CharField(max_length=255, verbose_name="Текст вопроса")
    anwser1 = models.CharField(max_length=100, verbose_name="Композитор")
    answer2 = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    audiofile = models.FileField(upload_to="quiz_audio/")

    def __str__(self):
        resName = f"Аудио: {self.anwser1}  {self.answer2}"
        if self.comment:
            resName += f" {self.comment}"
        return  resName

    class Meta:
        verbose_name = "Аудио вопрос"
        verbose_name_plural = "Аудио вопросы"
        ordering = ["id"]

class Quiz_result(models.Model):
    user_id = models.CharField
    date_time = models.DateTimeField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)

    def __str__(self):
        return "Результаты тестирования (" + self.quiz.title

    class Meta:
        verbose_name = "Результат викторины"
        verbose_name_plural = "Результаты викторин"
        ordering = ["-date_time"]






class Answer(models.Model):
    quiz_result = models.ForeignKey(Quiz_result, related_name="AnswersList", on_delete=models.PROTECT)
    question = models.ForeignKey(Question_audio, verbose_name="вопрос", on_delete=models.PROTECT)
    answer1 = models.CharField(max_length=100, verbose_name="Ответ1")
    answer2 = models.CharField(max_length=100, verbose_name="Ответ 2", blank=True)

    def __str__(self):
        return f"Ответ 1. {self.answer1} Ответ 2. {self.answer2}"

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["quiz_result"]







