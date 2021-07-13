from django.db import models

# Create your models here.

#we are not going to use this model, I just wanted to test out things.... NO need to worry about that
class Simple(models.Model):
    test = models.CharField(max_length=100)
    newfld = models.CharField(max_length=100)
