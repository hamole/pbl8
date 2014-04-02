# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Study'
        db.create_table(u'pbl_study', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2014, max_length=4)),
            ('funder', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'pbl', ['Study'])

        # Adding M2M table for field treatment on 'Study'
        m2m_table_name = db.shorten_name(u'pbl_study_treatment')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('study', models.ForeignKey(orm[u'pbl.study'], null=False)),
            ('treatment', models.ForeignKey(orm[u'pbl.treatment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['study_id', 'treatment_id'])

        # Deleting field 'Treatment.effective'
        db.delete_column(u'pbl_treatment', 'effective')

        # Adding field 'Treatment.slug'
        db.add_column(u'pbl_treatment', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='homeopathy', max_length=50),
                      keep_default=False)

        # Adding field 'Treatment.description'
        db.add_column(u'pbl_treatment', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Study'
        db.delete_table(u'pbl_study')

        # Removing M2M table for field treatment on 'Study'
        db.delete_table(db.shorten_name(u'pbl_study_treatment'))

        # Adding field 'Treatment.effective'
        db.add_column(u'pbl_treatment', 'effective',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Treatment.slug'
        db.delete_column(u'pbl_treatment', 'slug')

        # Deleting field 'Treatment.description'
        db.delete_column(u'pbl_treatment', 'description')


    models = {
        u'pbl.study': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Study'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'funder': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'treatment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pbl.Treatment']", 'symmetrical': 'False'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2014', 'max_length': '4'})
        },
        u'pbl.treatment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Treatment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pbl']