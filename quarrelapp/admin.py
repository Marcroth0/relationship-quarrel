from django.contrib import admin
from .models import Post, Comment, CommentPost


admin.site.register(Post)
admin.site.register(CommentPost)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_published')
    search_fields = ('name', 'email', 'body')
