# Generated by Django 3.2 on 2022-02-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quarrelapp', '0008_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(choices=[('CLEANING', 'Cleaning'), ('JEALOUSY', 'Jealousy'), ('YOUNEVER', 'You never'), ('OTHER', 'Other')], default='CLEANING', max_length=13),
        ),
    ]
