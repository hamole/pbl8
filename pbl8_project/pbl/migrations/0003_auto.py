# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field studies_for on 'Treatment'
        m2m_table_name = db.shorten_name(u'pbl_treatment_studies_for')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('treatment', models.ForeignKey(orm[u'pbl.treatment'], null=False)),
            ('study', models.ForeignKey(orm[u'pbl.study'], null=False))
        ))
        db.create_unique(m2m_table_name, ['treatment_id', 'study_id'])

        # Adding M2M table for field studies_against on 'Treatment'
        m2m_table_name = db.shorten_name(u'pbl_treatment_studies_against')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('treatment', models.ForeignKey(orm[u'pbl.treatment'], null=False)),
            ('study', models.ForeignKey(orm[u'pbl.study'], null=False))
        ))
        db.create_unique(m2m_table_name, ['treatment_id', 'study_id'])

        # Removing M2M table for field treatment on 'Study'
        db.delete_table(db.shorten_name(u'pbl_study_treatment'))


    def backwards(self, orm):
        # Removing M2M table for field studies_for on 'Treatment'
        db.delete_table(db.shorten_name(u'pbl_treatment_studies_for'))

        # Removing M2M table for field studies_against on 'Treatment'
        db.delete_table(db.shorten_name(u'pbl_treatment_studies_against'))

        # Adding M2M table for field treatment on 'Study'
        m2m_table_name = db.shorten_name(u'pbl_study_treatment')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('study', models.ForeignKey(orm[u'pbl.study'], null=False)),
            ('treatment', models.ForeignKey(orm[u'pbl.treatment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['study_id', 'treatment_id'])


    models = {
        u'pbl.study': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Study'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'funder': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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