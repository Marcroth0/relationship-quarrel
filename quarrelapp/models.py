from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import timezone

User = settings.AUTH_USER_MODEL_USER


class ContentPost(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()

    CLEANING = "CLN"
    JEALOUSY = "JLY"
    YOUNEVER = "YNR"
    OTHER = "OTH"

    TITLE_CHOICES = [
        (CLEANING, 'Cleaning'),
        (JEALOUSY, 'Jealousy'),
        (YOUNEVER, 'You never...'),
        (OTHER, 'Other'),
    ]
    title = models.CharField(
        max_length=2,
        choices=TITLE_CHOICES,
        default=CLEANING,
    )
    date_published = models.DateField(default=timezone.now)
    url = models.SlugField(max_length=500, unique=True,
                           blank=True, editable=False)
    likes = models.ManyToManyField(
        User, related_name='content_like', blank=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(ContentPost, self).save(*args, **kwargs)
