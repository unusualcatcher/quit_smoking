# Generated by Django 5.0.1 on 2024-01-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='listened_to_hypnotune_today',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_hypnotunes_listened',
            field=models.PositiveIntegerField(default=0),
        ),
    ]