from django import forms
from .models import Question_Banks_Main, Questions_Main, Question_Module, SubQuestions

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
    OPTION = ()
    OPTION2 = ()
    QP_name = forms.CharField(max_length=150)
    Question_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTION)
    Question_Module_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              choices=OPTION2)

class QuestionBankRenameForm(forms.ModelForm):
    class Meta:
        model = Question_Banks_Main
        fields = ('name',)

class QuestionModuleForm(forms.ModelForm):
    class Meta:
        model = Question_Module
        fields = ('statement', 'subquestions')

class SubQuestionForm(forms.ModelForm):
    class Meta:
        model = SubQuestions
        fields = ('statement', 'answer', 'marks', 'difficulty', 'tag')
        # exclude = ['username', 'file']