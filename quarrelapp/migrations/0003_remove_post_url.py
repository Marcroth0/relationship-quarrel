# Generated by Django 3.2 on 2022-01-26 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quarrelapp', '0002_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]