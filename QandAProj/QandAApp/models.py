from django.db import models

# Create your models here.
class QandAModel(models.Model):
    question = models.CharField(max_length=128, unique=True)
    answer = models.CharField(max_length=128)
    header = models.CharField(max_length=128)
