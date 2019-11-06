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
# class SetPasswordForm(forms.Form):
# 	"""
#     A form that lets a user change set their password without entering the old
#     password
#     """
# 	error_messages = {
# 		'password_mismatch': _("The two password fields didn't match."),
# 	}
# 	new_password1 = forms.CharField(label=_("New password"),
# 	                                widget=forms.PasswordInput)
# 	new_password2 = forms.CharField(label=_("New password confirmation"),
# 	                                widget=forms.PasswordInput)

#     # def __init__(self, user, *args, **kwargs):
#     #     self.user = user
#     #     super(SetPasswordForm, self).__init__(*args, **kwargs)
# 	def __init__(self, *args, **kwargs):
# 		request = kwargs.pop("request") # it's best you pop request, so that you don't get any complains for a parent that checks what kwargs it gets
# 		super(MyPasswordChangeForm, self).__init__(request.user, *args, **kwargs)

# 	def clean_new_password2(self):
# 		password1 = self.cleaned_data.get('new_password1')
# 		password2 = self.cleaned_data.get('new_password2')
# 		if password1 and password2:
# 		    if password1 != password2:
# 		        raise forms.ValidationError(
# 	 	        	self.error_messages['password_mismatch'],
# 		        	code='password_mismatch',
# 				)
# 		return password2

# 	def save(self, commit=True):
# 	    self.user.set_password(self.cleaned_data['new_password1'])
# 	    if commit:
# 	        self.user.save()
# 	    return self.user

# class PasswordChangeForm(SetPasswordForm):
# 	"""
# 	A form that lets a user change their password by entering their old
# 	password.
# 	"""
# 	error_messages = dict(SetPasswordForm.error_messages, **{
#     	'password_incorrect': _("Your old password was entered incorrectly. "
# 							    "Please enter it again."),
# 	})
# 	old_password = forms.CharField(label=_("Old password"),
# 	                               widget=forms.PasswordInput)

# 	def clean_old_password(self):
# 		"""
# 	    Validates that the old_password field is correct.
#         """
# 		old_password = self.cleaned_data["old_password"]
# 		if not self.user.check_password(old_password):
# 		    raise forms.ValidationError(
# 		        self.error_messages['password_incorrect'],
# 		        code='password_incorrect',
# 	        )
# 		return old_password


# 		PasswordChangeForm.base_fields = OrderedDict(
#     			(k, PasswordChangeForm.base_fields[k])
#     	for k in ['old_password', 'new_password1', 'new_password2']
# 		)


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChangePassword(generic.CreateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('logout')
    template_name = 'password_change.html'

    # def get_form_kwargs(self, **kwargs):
    #     data = super(ChangePassword, self).get_form_kwargs(**kwargs)
    #     data['request'] = self.request
    #     return data    
# class UpdateProfile(forms.ModelForm):
#     username = forms.CharField(required=True)
#     class Meta:
#         model = User
#         fields = ('username')

#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         # user.email = self.cleaned_data['email']

#         if commit:
#             user.save()

#         return user
