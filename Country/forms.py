from django import forms
from .models import CountryComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = CountryComment
        fields = [
            'text',
        ]
