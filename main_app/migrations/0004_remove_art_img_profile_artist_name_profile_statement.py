# Generated by Django 4.0.6 on 2022-07-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_profile_photoprofile_photoart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='img',
        ),
        migrations.AddField(
            model_name='profile',
            name='artist_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='statement',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
