from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 100)
    mother_alphabet = models.CharField(max_length = 20)
