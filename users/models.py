from django.db import models

class Language(models.Model):
    name = models.CharField(max_length = 50)
    img = models.CharField(max_length = 255)

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
