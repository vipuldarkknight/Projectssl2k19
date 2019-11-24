import django_filters
from .models import Questions_Main, SubQuestions

class QuestionsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Questions_Main
        fields={
            'statement':['icontains'],
            'marks':['exact'],
            'difficulty':['exact'],
            'tag':['icontains']}


class SubQuestionsFilter(django_filters.FilterSet):
    class Meta:
        model = SubQuestions
        fields = {
            'statement': ['icontains'],
            'marks': ['exact'],
            'difficulty': ['exact'],
            'tag': ['icontains']}
