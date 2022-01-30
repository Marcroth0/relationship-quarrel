from django import forms
from crispy_forms.helper import FormHelper
from .models import Comment, Post
from crispy_forms.layout import (Field, Layout, Row, Column, Submit)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content_one', 'content_two', 'title', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
