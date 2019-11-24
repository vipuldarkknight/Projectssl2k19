from django.db import models
from django.forms import ModelForm

# Create your models here.
class Question_Banks_Main(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='question_banks/', blank=True, null=True)

    def __str__(self):
        return self.name


class Questions_Main(models.Model):

    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    username = models.CharField(max_length=150)
    qb_name = models.CharField(max_length=50)
    statement = models.TextField()
    answer = models.TextField(blank=True, null=True)
    marks = models.IntegerField()
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES, default=EASY)
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

class created_paper(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    num_ques = models.IntegerField()
    marks = models.IntegerField()
    ques_id = models.CharField(max_length=150)
    num_ques_modules=models.IntegerField()
    ques_module_id = models.CharField(max_length=150)
    total_sum_ques = models.IntegerField()
    duration = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Question_Module(models.Model):
    username = models.CharField(max_length=150)
    qb_name = models.CharField(max_length=50)
    statement = models.TextField()
    marks = models.IntegerField()
    subquestions = models.IntegerField()
    ques_id_string = models.CharField(max_length=150)

    def __str__(self):
        return self.statement

class SubQuestions(models.Model):

    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    question_module_id = models.IntegerField()
    statement = models.TextField()
    answer = models.TextField(blank=True, null=True)
    marks = models.IntegerField()
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES, default=EASY)
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

