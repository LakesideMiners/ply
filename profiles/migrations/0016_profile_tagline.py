# Generated by Django 4.0.2 on 2022-02-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tagline',
            field=models.TextField(default='', verbose_name='Profile Tagline'),
            preserve_default=False,
        ),
    ]
