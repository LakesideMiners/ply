# Generated by Django 4.0.4 on 2022-05-21 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0014_streammessage_likes_streammessage_reposts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='streammessage',
            name='references',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stream.streammessage', verbose_name='References'),
        ),
    ]
