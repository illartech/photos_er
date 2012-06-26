# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'tblUsers', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=192, db_column='UserName')),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=192, db_column='Password')),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=384, db_column='Email', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=384, db_column='Name', blank=True)),
            ('lastlogindate', self.gf('django.db.models.fields.DateTimeField')(db_column='LastLoginDate')),
            ('hash', self.gf('django.db.models.fields.CharField')(max_length=384, db_column='Hash', blank=True)),
            ('authlevel', self.gf('django.db.models.fields.IntegerField')(db_column='AuthLevel')),
        ))
        db.send_create_signal('gallery', ['User'])

        # Adding model 'Album'
        db.create_table(u'tblAlbums', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], null=True, db_column='ParentAlbumId', blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='AlbumName')),
            ('description', self.gf('django.db.models.fields.TextField')(db_column='AlbumDescription', blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Keywords', blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 24, 0, 0), db_column='AlbumDate')),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 24, 0, 0), db_column='DateCreated')),
            ('datelastmodified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 24, 0, 0), db_column='DateLastModified')),
            ('published', self.gf('django.db.models.fields.IntegerField')(default=1, db_column='Published')),
            ('passwordprotected', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='PasswordProtected')),
        ))
        db.send_create_signal('gallery', ['Album'])

        # Adding model 'Photo'
        db.create_table(u'tblPhotos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('photodate', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='PhotoDate', blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Title', blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Description', blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Location', blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Keywords', blank=True)),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 24, 0, 0), db_column='DateCreated')),
            ('datelastmodified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 24, 0, 0), db_column='DateLastModified')),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], db_column='Album')),
            ('order', self.gf('django.db.models.fields.IntegerField')(db_column='PhotoOrder')),
        ))
        db.send_create_signal('gallery', ['Photo'])

        # Adding model 'Notification'
        db.create_table(u'tblNotification', (
            ('idx', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(db_column='Name')),
            ('email', self.gf('django.db.models.fields.TextField')(db_column='Email')),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')(db_column='LastUpdate')),
            ('active', self.gf('django.db.models.fields.IntegerField')(db_column='Active')),
        ))
        db.send_create_signal('gallery', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'tblUsers')

        # Deleting model 'Album'
        db.delete_table(u'tblAlbums')

        # Deleting model 'Photo'
        db.delete_table(u'tblPhotos')

        # Deleting model 'Notification'
        db.delete_table(u'tblNotification')


    models = {
        'gallery.album': {
            'Meta': {'object_name': 'Album', 'db_table': "u'tblAlbums'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'db_column': "'AlbumDate'"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'db_column': "'DateCreated'"}),
            'datelastmodified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'db_column': "'DateLastModified'"}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'AlbumDescription'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Keywords'", 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Album']", 'null': 'True', 'db_column': "'ParentAlbumId'", 'blank': 'True'}),
            'passwordprotected': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'PasswordProtected'"}),
            'published': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_column': "'Published'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'AlbumName'"})
        },
        'gallery.notification': {
            'Meta': {'object_name': 'Notification', 'db_table': "u'tblNotification'"},
            'active': ('django.db.models.fields.IntegerField', [], {'db_column': "'Active'"}),
            'email': ('django.db.models.fields.TextField', [], {'db_column': "'Email'"}),
            'idx': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "'LastUpdate'"}),
            'name': ('django.db.models.fields.TextField', [], {'db_column': "'Name'"})
        },
        'gallery.photo': {
            'Meta': {'ordering': "['order', 'photodate']", 'object_name': 'Photo', 'db_table': "u'tblPhotos'"},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Album']", 'db_column': "'Album'"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'db_column': "'DateCreated'"}),
            'datelastmodified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'db_column': "'DateLastModified'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Description'", 'blank': 'True'}),
            'filename': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Keywords'", 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Location'", 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'db_column': "'PhotoOrder'"}),
            'photodate': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'PhotoDate'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Title'", 'blank': 'True'})
        },
        'gallery.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'tblUsers'"},
            'authlevel': ('django.db.models.fields.IntegerField', [], {'db_column': "'AuthLevel'"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '384', 'db_column': "'Email'", 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '384', 'db_column': "'Hash'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'lastlogindate': ('django.db.models.fields.DateTimeField', [], {'db_column': "'LastLoginDate'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '384', 'db_column': "'Name'", 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '192', 'db_column': "'Password'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '192', 'db_column': "'UserName'"})
        }
    }

    complete_apps = ['gallery']