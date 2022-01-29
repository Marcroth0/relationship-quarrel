from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import string
import random

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class CommentPost(models.Model):
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True)


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    content_one = models.OneToOneField(
        CommentPost, on_delete=models.CASCADE, related_name="content_post_one")
    content_two = models.OneToOneField(
        CommentPost, on_delete=models.CASCADE, related_name="content_post_two")
    description = models.TextField(default='')

    CLEANING = "CLN"
    JEALOUSY = "JLY"
    YOUNEVER = "YNR"
    OTHER = "OTH"

    TITLE_CHOICES = [
        (CLEANING, 'Cleaning'),
        (JEALOUSY, 'Jealousy'),
        (YOUNEVER, 'You never'),
        (OTHER, 'Other'),
    ]
    title = models.CharField(
        max_length=13,
        choices=TITLE_CHOICES,
        default=CLEANING,
    )
    slug = models.SlugField(max_length=255, unique=True)
    date_published = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='content_likes', blank=True)

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
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    CONTENTONE = "CTONE"
    CONTENTTWO = "CTTWO"
    UNDECIDED = "UND"

    QUARREL_CHOICES = [
        (CONTENTONE, 'Left'),
        (UNDECIDED, 'Undecided'),
        (CONTENTTWO, 'Right')
    ]
    quarrel_choice = models.CharField(
        max_length=14,
        choices=QUARREL_CHOICES,
        default=UNDECIDED,
    )
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_published"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# @receiver(pre_save, sender=Post)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
