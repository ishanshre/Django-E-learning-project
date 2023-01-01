from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from phonenumber_field.widgets import PhoneNumberPrefixWidget

from user.models import Profile

from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        field = ['username','email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','date_of_birth', 'email_verified']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(initial=False, required=False)
    
    class Meta:
        model = User
        fields = ['username','password','remember_me']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','gender','country','phone','github','twitter','linkedin']
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial="NP")
        }

class UserForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','date_of_birth']
        