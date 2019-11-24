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
    Duration = forms.CharField(max_length=150)
    Question_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTION)
    Question_Module_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              choices=OPTION2)

class SingleCorrectForm(forms.Form):

    ANSWER_CHOICES = [
        ("", 'Select'),
        ("A", 'Choice1'),
        ("B", 'Choice2'),
        ("C", 'Choice3'),
        ("D", 'Choice4'),
    ]

    Choice1 = forms.CharField()
    Choice2 = forms.CharField()
    Choice3 = forms.CharField()
    CHoice4 = forms.CharField()
    Answer = forms.CharField(label="Answer",widget=forms.Select(choices=ANSWER_CHOICES ), required = False)

class MatchtheColumnForm(forms.Form):

    ANSWER_CHOICES = [
        ("", 'Select'),
        ("A", 'A'),
        ("B", 'B'),
        ("C", 'C'),
        ("D", 'D'),
    ]

    Choice1 = forms.CharField()
    Choice2 = forms.CharField()
    Choice3 = forms.CharField()
    CHoice4 = forms.CharField()
    Answer1 = forms.CharField(label="Answer1",widget=forms.Select(choices=ANSWER_CHOICES ), required = False)
    Answer2 = forms.CharField(label="Answer2",widget=forms.Select(choices=ANSWER_CHOICES ), required = False)
    Answer3 = forms.CharField(label="Answer3",widget=forms.Select(choices=ANSWER_CHOICES ), required = False)
    Answer4 = forms.CharField(label="Answer4",widget=forms.Select(choices=ANSWER_CHOICES ), required = False)

class MatchtheColumn2Form(forms.Form):

    A = forms.CharField()
    B = forms.CharField()
    C = forms.CharField()
    D = forms.CharField()
    


class MultiCorrectForm(forms.Form):
    OPTION = (
        ("a", "Choice1"),
        ("b", "Choice2"),
        ("c", "Choice3"),
        ("d", "Choice4"),
    )
    # OPTION2 = ()
    # QP_name = forms.CharField(max_length=150)
    # Duration = forms.CharField(max_length=150)
    Choice1 = forms.CharField()
    Choice2 = forms.CharField()
    Choice3 = forms.CharField()
    CHoice4 = forms.CharField()
    Choose_Answers = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTION, required=False)
    # Question_Module_List = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            #   choices=OPTION2)

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
    difficulty = forms.CharField(label="difficulty",widget=forms.Select(choices=DIFFICULTY_CHOICES))
    tag = forms.CharField(max_length=150)

    

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
