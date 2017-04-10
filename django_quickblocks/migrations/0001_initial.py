# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-10 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was originally created')),
                ('modified_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was last modified')),
                ('title', models.CharField(blank=True, help_text=b'The title for this block of content, optional', max_length=255, null=True)),
                ('summary', models.TextField(blank=True, help_text=b'The summary for this item, should be short', null=True)),
                ('content', models.TextField(blank=True, help_text=b'The body of text for this content block, optional', null=True)),
                ('image', models.ImageField(blank=True, help_text=b'Any image that should be displayed with this content block, optional', null=True, upload_to=b'quickblocks')),
                ('color', models.CharField(blank=True, help_text=b'A background color to use for the image, in the format: #rrggbb', max_length=16, null=True)),
                ('link', models.CharField(blank=True, help_text=b'Any link that should be associated with this content block, optional', max_length=255, null=True)),
                ('video_id', models.CharField(blank=True, help_text=b'The id of the YouTube video that should be linked to this item', max_length=255, null=True)),
                ('tags', models.CharField(blank=True, help_text=b'Any tags for this content block, separated by spaces, can be used to do more advanced filtering, optional', max_length=255, null=True)),
                ('priority', models.IntegerField(default=0, help_text=b'The priority for this block, higher priority blocks come first')),
                ('created_by', models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblock_creations', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblock_modifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuickBlockImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was originally created')),
                ('modified_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was last modified')),
                ('image', models.ImageField(height_field=b'height', upload_to=b'quickblock_images/', width_field=b'width')),
                ('caption', models.CharField(max_length=64)),
                ('priority', models.IntegerField(blank=True, default=0, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('created_by', models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblockimage_creations', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblockimage_modifications', to=settings.AUTH_USER_MODEL)),
                ('quickblock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='django_quickblocks.QuickBlock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuickBlockType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was originally created')),
                ('modified_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, help_text='When this item was last modified')),
                ('name', models.CharField(help_text=b'The human readable name for this content type', max_length=75, unique=True)),
                ('slug', models.SlugField(help_text=b'The slug to idenfity this content type, used with the template tags', unique=True)),
                ('description', models.TextField(blank=True, help_text=b'A description of where this content type is used on the site and how it will be dsiplayed', null=True)),
                ('has_title', models.BooleanField(default=True, help_text=b'Whether this content should include a title')),
                ('has_image', models.BooleanField(default=True, help_text=b'Whether this content should include an image')),
                ('has_rich_text', models.BooleanField(default=True, help_text=b'Whether this content should use a rich HTML editor')),
                ('has_summary', models.BooleanField(default=True, help_text=b'Whether this content should include a summary field')),
                ('has_link', models.BooleanField(default=True, help_text=b'Whether this content should include a link')),
                ('has_gallery', models.BooleanField(default=False, help_text=b'Whether this content should allow upload of additional images, ie a gallery')),
                ('has_color', models.BooleanField(default=False, help_text=b'Whether this content has a color field')),
                ('has_video', models.BooleanField(default=False, help_text=b'Whether this content should allow setting a YouTube id')),
                ('has_tags', models.BooleanField(default=False, help_text=b'Whether this content should allow tags')),
                ('created_by', models.ForeignKey(help_text='The user which originally created this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblocktype_creations', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='django_quickblocks_quickblocktype_modifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='quickblock',
            name='quickblock_type',
            field=models.ForeignKey(help_text=b'The category, or type for this content block', on_delete=django.db.models.deletion.CASCADE, to='django_quickblocks.QuickBlockType', verbose_name=b'Content Type'),
        ),
    ]
