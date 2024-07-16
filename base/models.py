from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.CharField(max_length=255)
    imgSrc = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class UserScore(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    score = models.CharField(max_length=2)

    def __str__(self):
        return self.score