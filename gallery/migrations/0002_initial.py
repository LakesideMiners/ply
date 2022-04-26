# Generated by Django 4.0.2 on 2022-04-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('gallery', '0001_initial'),
        ('profiles', '0001_initial'),
        ('keywords', '0001_initial'),
        ('community', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerytempfile',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Profile'),
        ),
        migrations.AddField(
            model_name='galleryitemkeyword',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.galleryitem', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='galleryitemkeyword',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='keywords.keyword', verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='galleryitemfile',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.galleryitem', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='galleryitemcomments',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.galleryitem', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='galleryitemcomments',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='galleryitemcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.galleryartworkcat', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='galleryitemcategory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gallery.galleryitem', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='galleryitem',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Item Owner'),
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallerycollection', verbose_name='Gallery Collection'),
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.community', verbose_name='Community'),
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='group.group', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='gallerycollectionpermission',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Profile'),
        ),
        migrations.AddField(
            model_name='gallerycollectionitems',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallerycollection', verbose_name='Collection'),
        ),
        migrations.AddField(
            model_name='gallerycollectionitems',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.galleryitem', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='gallerycatgroupobject',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.galleryartworkcat', verbose_name='Gallery Category'),
        ),
        migrations.AddField(
            model_name='gallerycatgroupobject',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallerycatgroups', verbose_name='Gallery Category Parent Group'),
        ),
    ]
