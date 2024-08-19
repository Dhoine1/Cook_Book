from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from TuliusCookBook.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Логин ")
    password1 = forms.CharField(label="Пароль ")
    password2 = forms.CharField(label="Подтвердите пароль ")
    email = forms.EmailField(label="Email ")

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
        )


# форма для создания профиля
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'nikname', 'signature']

        widgets = {
            'signature': forms.Textarea(attrs={'rows': 1, 'cols': 50})
        }
