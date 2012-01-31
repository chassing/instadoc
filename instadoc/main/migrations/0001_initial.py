# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Documentation'
        db.create_table('main_documentation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='docs', to=orm['main.Category'])),
        ))
        db.send_create_signal('main', ['Documentation'])

        # Adding model 'Category'
        db.create_table('main_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=254, blank=True)),
        ))
        db.send_create_signal('main', ['Category'])


    def backwards(self, orm):
        
        # Deleting model 'Documentation'
        db.delete_table('main_documentation')

        # Deleting model 'Category'
        db.delete_table('main_category')


    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'})
        },
        'main.documentation': {
            'Meta': {'object_name': 'Documentation'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'docs'", 'to': "orm['main.Category']"}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['main']
