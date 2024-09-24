from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from TuliusCookBook.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Логин ")
    password1 = forms.CharField(label="Пароль ", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Подтвердите пароль ", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise forms.ValidationError("В имени не должно быть пробелов")
        elif User.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой пользователь уже есть")
        return username

    def clean_password2(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError("Пароли не совпадают")
        return pass2

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
