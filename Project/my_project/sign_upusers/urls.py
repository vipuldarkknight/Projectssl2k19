from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('changepassword/', views.ChangePassword.as_view(), name='password_chng'),    
]