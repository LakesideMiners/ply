# Generated by Django 4.0.2 on 2022-02-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_groupmember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_id',
        ),
    ]
