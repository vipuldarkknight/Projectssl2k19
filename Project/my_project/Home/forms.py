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