from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.forms import RegestrationForm

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

class UserChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField(label=_("Password"),
    #     help_text=_("Raw passwords are not stored, so there is no way to see "
    #                 "this user's password, but you can change the password "
    #                 "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = User
        fields = (
            # 'username',
            'first_name',
            'last_name',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


def edit_profile(request):
	if request.method == 'POST':
		form=UserChangeForm(request.POST,instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return redirect('logout')
	else:
		form = UserChangeForm(instance=request.user)
		args={'form':form}
		return render(request,'edit_profile.html',args)

# def change_password(request):
# 	if request.method == 'POST':
# 		form=PasswordChangeForm(request.user,request.POST,instance=request.user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('home')
# 		else:
# 			return redirect('logout')
# 	else:
# 		form = PasswordChangeForm(instance=request.user)
# 		args={'form':form}
# 		return render(request,'change_password.html',args)

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
