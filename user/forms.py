from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        field = ['username','email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','date_of_birth', 'email_verified']
