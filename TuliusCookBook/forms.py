from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import *


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'dish_name',
            'description',
            'ingredient',
            'recipe_text',
            'image',
            'story',
            'section',
            'author'
        ]

        widgets = {"dish_name": forms.Textarea(attrs={'rows': 2}),
                   'description': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name='extends'),
                   'ingredient': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name='extends'),
                   'recipe_text': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name='extends'),
                   'section': forms.Select(attrs={'width': 177})
                   }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
