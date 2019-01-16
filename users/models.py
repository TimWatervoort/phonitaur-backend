from django.db import models

class Language(models.Model):
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 255)
    text_color = models.CharField(max_length = 20, default='text-white')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 100)
    mother_alphabet = models.CharField(max_length = 20)
    img = models.CharField(max_length = 255, default=None, blank=True, null=True)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.username

class Lesson(models.Model):
    name = models.CharField(max_length = 50)
    language = models.IntegerField()
    icon = models.CharField(max_length = 255, blank=True, null=True)

    def __str__(self):
        return self.name
