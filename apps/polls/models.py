import datetime

from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField('Название опроса', max_length=255)
    start_date = models.DateTimeField('Дата старта')
    end_date = models.DateTimeField('Дата окончания')
    description = models.TextField(null=True, blank=True)

    @property
    def is_active(self):
        now = datetime.datetime.now()
        return self.start_date <= now < self.end_date

    def __str__(self):
        return self.name


class Question(models.Model):
    TEXT_ANSWER = 'text_answer'
    SINGLE_ANSWER = 'single_answer'
    MULTIPLE_ANSWERS = 'multiple_answers'
    QUESTION_TYPES = (
        (TEXT_ANSWER, 'Ответ текстом'),
        (SINGLE_ANSWER, 'Ответ с одним правильным вариантом'),
        (MULTIPLE_ANSWERS, 'Ответ с несколькими правильными вариантами')
    )
    text = models.TextField('Текст вопроса')
    type = models.CharField('Тип вопроса', choices=QUESTION_TYPES, max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Variant(models.Model):
    value = models.CharField('Вариант ответа', max_length=255, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        if self.value == '':
            return f'Ответ'
        return self.value


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_user')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='report_poll')
    created = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vote_user')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='vote_poll')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='vote_question')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='vote_variant', blank=True, null=True)
    text = models.TextField('Ответ текстом', blank=True, null=True)
