# Generated by Django 4.0.4 on 2022-05-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SLHUD', '0003_alter_slagent_uuid_alter_slparcel_uuid_slparcelagent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slparcelagent',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active FLAG'),
        ),
        migrations.AlterField(
            model_name='slparcelagent',
            name='online',
            field=models.BooleanField(default=False, verbose_name='Online FLAG'),
        ),
    ]
