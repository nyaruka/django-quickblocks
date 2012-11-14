# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QuickBlockImage.is_active'
        db.add_column('django_quickblocks_quickblockimage', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'QuickBlockImage.created_by'
        db.add_column('django_quickblocks_quickblockimage', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='quickblockimage_creations', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'QuickBlockImage.created_on'
        db.add_column('django_quickblocks_quickblockimage', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime.now(), blank=True),
                      keep_default=False)

        # Adding field 'QuickBlockImage.modified_by'
        db.add_column('django_quickblocks_quickblockimage', 'modified_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='quickblockimage_modifications', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'QuickBlockImage.modified_on'
        db.add_column('django_quickblocks_quickblockimage', 'modified_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime.now(), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'QuickBlockImage.is_active'
        db.delete_column('django_quickblocks_quickblockimage', 'is_active')

        # Deleting field 'QuickBlockImage.created_by'
        db.delete_column('django_quickblocks_quickblockimage', 'created_by_id')

        # Deleting field 'QuickBlockImage.created_on'
        db.delete_column('django_quickblocks_quickblockimage', 'created_on')

        # Deleting field 'QuickBlockImage.modified_by'
        db.delete_column('django_quickblocks_quickblockimage', 'modified_by_id')

        # Deleting field 'QuickBlockImage.modified_on'
        db.delete_column('django_quickblocks_quickblockimage', 'modified_on')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'django_quickblocks.quickblock': {
            'Meta': {'object_name': 'QuickBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblock_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblock_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quickblock_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_quickblocks.QuickBlockType']"}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'django_quickblocks.quickblockimage': {
            'Meta': {'object_name': 'QuickBlockImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblockimage_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblockimage_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'quickblock': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['django_quickblocks.QuickBlock']"}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'django_quickblocks.quickblocktype': {
            'Meta': {'object_name': 'QuickBlockType'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblocktype_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'has_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_image': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_link': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_rich_text': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_summary': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quickblocktype_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['django_quickblocks']
