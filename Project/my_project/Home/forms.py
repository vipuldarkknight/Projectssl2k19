from django import forms
from .models import Question_Banks_Main, Questions_Main

class QuestionBankForm(forms.ModelForm):
    class Meta:
        model = Question_Banks_Main
        # fields = ('username', 'name', 'file')
        exclude = ['username', 'file']

class QuestionBankForm2(forms.ModelForm):
    class Meta:
        model = Question_Banks_Main
        # fields = ('username', 'name', 'file')
        exclude = ['username', 'name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions_Main
        fields = ('statement', 'answer', 'marks', 'difficulty', 'tag')
        # exclude = ['username', 'file']

class CountryForm(forms.Form):
    OPTION = (
    )
    QP_name = forms.CharField(max_length=150)
    Question_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTION)

class SingleCorrectForm(forms.Form):

    ANSWER_CHOICES = [
        ("A", 'Choice1'),
        ("B", 'Choice2'),
        ("C", 'Choice3'),
        ("D", 'Choice4'),
    ]

    Choice1 = forms.CharField()
    Choice2 = forms.CharField()
    Choice3 = forms.CharField()
    CHoice4 = forms.CharField()
    Answer = forms.CharField(label="Answer",widget=forms.Select(choices=ANSWER_CHOICES ))

class MCQForm(forms.Form):

    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    statement = forms.CharField(max_length=500)
    # Author = forms.CharField()
    marks = forms.IntegerField()
    difficulty = forms.CharField(label="difficulty",widget=forms.Select(choices=DIFFICULTY_CHOICES  ))
    tag = forms.CharField(max_length=150)