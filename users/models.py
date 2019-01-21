from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Language(models.Model):
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 255)
    text_color = models.CharField(max_length = 20, default='text-white')

    def __str__(self):
        return self.name

class PhonitaurUser(AbstractUser):
    mother_alphabet = models.CharField(max_length = 20)
    img = models.CharField(max_length = 255, default=None, blank=True, null=True)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 255)

    def __str__(self):
        return self.question_text

class Lesson(models.Model):
    name = models.CharField(max_length = 50)
    language = models.CharField(max_length=50)
    icon = models.CharField(max_length = 255, blank=True, null=True)
    level = models.IntegerField(default=1)
    lesson_text = models.TextField(default="")
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
