# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Treatment'
        db.create_table(u'pbl_treatment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('effective', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'pbl', ['Treatment'])


    def backwards(self, orm):
        # Deleting model 'Treatment'
        db.delete_table(u'pbl_treatment')


    models = {
        u'pbl.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'effective': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pbl']