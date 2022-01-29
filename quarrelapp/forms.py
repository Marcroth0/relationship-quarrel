from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content_one', 'content_two', 'title')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
