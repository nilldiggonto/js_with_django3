from django import forms
from .models import PostUp


class PostUpForm(forms.ModelForm):
    class Meta:
        model = PostUp
        fields = ('image','title','content')