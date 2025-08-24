from django import forms
from django.template.defaulttags import widthratio

from .models import Movie, Genre


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = ['title', 'year', 'description', 'photo', 'video', 'genre']
        exclude = ['views']
        labels = {"title": "Kino nomi"}
        widgets = {
            'title': forms.TextInput(attrs={
                "style": "width: 300px; border-radius: 5px; padding: 5px;"
            }),
            'year': forms.NumberInput(attrs={
                "style": "width: 100px; border-radius: 5px; padding: 5px;"
            }),
            'description': forms.Textarea(attrs={
                "style": "border-radius: 5px; padding: 5px;"
            }),

        }