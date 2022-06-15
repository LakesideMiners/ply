# Generated by Django 4.0.4 on 2022-06-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Discipline Name')),
                ('hash', models.TextField(max_length=200, verbose_name='Hash')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('items', models.IntegerField(default=0, verbose_name='Item Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes Count')),
                ('dislikes', models.IntegerField(default=0, verbose_name='DisLikes Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Shares Count')),
                ('comments', models.IntegerField(default=0, verbose_name='Comment Count')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Category Name')),
                ('hash', models.TextField(max_length=200, verbose_name='Hash')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Item Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='tem Updated')),
                ('items', models.IntegerField(default=0, verbose_name='Item Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes Count')),
                ('dislikes', models.IntegerField(default=0, verbose_name='DisLikes Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Shares Count')),
                ('comments', models.IntegerField(default=0, verbose_name='Comment Count')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.discipline', verbose_name='Discipline Name')),
            ],
        ),
    ]
