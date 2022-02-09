from django.contrib import admin
from .models import Post, Comment, CommentPost


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_published')
    search_fields = ('name', 'email', 'body')


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('content',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content_one', 'content_two',
                    'date_published')
    list_filter = ('user', 'title')
