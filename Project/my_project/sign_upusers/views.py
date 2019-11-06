from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from braces.views import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import UpdateView
# from perfiles.models import Perfil

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
