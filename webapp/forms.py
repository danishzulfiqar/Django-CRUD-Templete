from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# Register user form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']


# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


# CreateRecord form
class CreateRecordForm(forms.ModelForm):
   class Meta:
         model = Record
         fields = ['name', 'email', 'phone', 'address']


# UpdateRecord form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'email', 'phone', 'address']
         