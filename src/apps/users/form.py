from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from apps.users.models import ExtendsUser


class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    password = forms.BooleanField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    
        
    class Meta:
    	model = User
    	fields = ('username', 'first_name', 'last_name', 'email', )



class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'style': 'background-color:black; color:grey;border-color: #242847;'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2', 'bio')

