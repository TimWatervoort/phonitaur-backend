from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 255)
    alphabet = models.CharField(max_length = 20)
    type_of = models.CharField(max_length = 20)

class Answer(models.Model):
    answer_text = models.CharField(max_length = 255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
