from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import RegestrationForm

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

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })        

