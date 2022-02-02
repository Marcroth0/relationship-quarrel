from django import forms
from crispy_forms.helper import FormHelper
from .models import Comment, Post
from crispy_forms.layout import (Field, Layout, Row, Column, Submit)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')

    content_one = forms.CharField(max_length=500)
    content_two = forms.CharField(max_length=500)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
