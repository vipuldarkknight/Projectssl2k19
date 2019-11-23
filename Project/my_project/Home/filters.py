import django_filters
from .models import Questions_Main

class QuestionsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Questions_Main
        fields={
            'statement':['icontains'],
            'marks':['exact'],
            'difficulty':['exact'],
            'tag':['icontains']}
