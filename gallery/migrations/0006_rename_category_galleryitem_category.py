# Generated by Django 4.0.4 on 2022-06-14 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_galleryitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryitem',
            old_name='Category',
            new_name='category',
        ),
    ]
