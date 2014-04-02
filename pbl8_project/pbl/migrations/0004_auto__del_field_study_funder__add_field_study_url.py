# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Study.funder'
        db.delete_column(u'pbl_study', 'funder')

        # Adding field 'Study.url'
        db.add_column(u'pbl_study', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Study.funder'
        db.add_column(u'pbl_study', 'funder',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'Study.url'
        db.delete_column(u'pbl_study', 'url')


    models = {
        u'pbl.study': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Study'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2014', 'max_length': '4'})
        },
        u'pbl.treatment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Treatment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'studies_against': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'studies_against+'", 'blank': 'True', 'to': u"orm['pbl.Study']"}),
            'studies_for': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'studies_for+'", 'blank': 'True', 'to': u"orm['pbl.Study']"})
        }
    }

    complete_apps = ['pbl']