from django.db import models
from django.forms import ModelForm


# Create your models here.
class Question_Banks_Main(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='question_banks/', blank=True, null=True)

    def __str__(self):
        return self.name
