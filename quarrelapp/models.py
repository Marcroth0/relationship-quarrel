from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import string
import random
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


def rand_slug():
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(6)
    )


class CommentPost(models.Model):
    """
    Content and likes model
    """
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def number_of_likes(self):
        return self.likes.count()


class Post(models.Model):
    """
    Post model
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    content_one = models.OneToOneField(
        CommentPost, on_delete=models.CASCADE, related_name="content_post_one"
    )
    content_two = models.OneToOneField(
        CommentPost, on_delete=models.CASCADE, related_name="content_post_two"
    )
    description = models.TextField(default="")

    CLEANING = "CLEANING"
    JEALOUSY = "JEALOUSY"
    YOUNEVER = "YOUNEVER"
    OTHER = "OTHER"

    TITLE_CHOICES = [
        (CLEANING, "Cleaning"),
        (JEALOUSY, "Jealousy"),
        (YOUNEVER, "You never"),
        (OTHER, "Other"),
    ]
    title = models.CharField(
        max_length=13,
        choices=TITLE_CHOICES,
        default=CLEANING,
    )
    slug = models.SlugField(max_length=255, unique=True)
    date_published = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="content_likes", blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=120)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_published"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
