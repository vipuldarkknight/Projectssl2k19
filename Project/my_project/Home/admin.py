from django.contrib import admin
from .models import Questions_Main, Question_Banks_Main

# Register your models here.
admin.site.register(Question_Banks_Main)
admin.site.register(Questions_Main)