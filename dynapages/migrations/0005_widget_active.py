# Generated by Django 4.0.4 on 2022-05-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynapages', '0004_widget_slhud'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active FLAG'),
        ),
    ]
