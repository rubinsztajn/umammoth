# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table('locations_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('locations', ['Room'])

        # Adding model 'LocationMap'
        db.create_table('locations_locationmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Room'])),
            ('shelf', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('accession', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accessions.Accession'], null=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umarmot.Collection'], null=True)),
        ))
        db.send_create_signal('locations', ['LocationMap'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table('locations_room')

        # Deleting model 'LocationMap'
        db.delete_table('locations_locationmap')


    models = {
        'accessions.accession': {
            'Meta': {'object_name': 'Accession'},
            'accretion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ack_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'boxes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'call_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'condition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_mat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date_rec': ('django.db.models.fields.DateField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'lin_ft': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rec_by': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'rec_method': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'restrictions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['addressbook.Contact']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'addressbook.contact': {
            'Meta': {'object_name': 'Contact'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grad_class': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mi': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'locations.locationmap': {
            'Meta': {'object_name': 'LocationMap'},
            'accession': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accessions.Accession']", 'null': 'True'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['umarmot.Collection']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Room']"}),
            'shelf': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'locations.room': {
            'Meta': {'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'umarmot.collection': {
            'Meta': {'object_name': 'Collection'},
            'accessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accessions.Accession']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['addressbook.Contact']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['locations']