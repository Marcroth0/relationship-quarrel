# Generated by Django 3.2 on 2022-02-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quarrelapp', '0006_auto_20220130_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(choices=[('CLEANING', 'Cleaning'), ('CLEANING', 'Jealousy'), ('YOUNEVER', 'You never'), ('OTHER', 'Other')], default='CLEANING', max_length=13),
        ),
    ]
