# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Accession'
        db.create_table('accessions_accession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('call_no', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('date_rec', self.gf('django.db.models.fields.DateField')()),
            ('date_mat', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('restrictions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lin_ft', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('boxes', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('items', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('condition', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rec_by', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('rec_method', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ack_date', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('accretion', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('accessions', ['Accession'])

        # Adding M2M table for field sources on 'Accession'
        db.create_table('accessions_accession_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accession', models.ForeignKey(orm['accessions.accession'], null=False)),
            ('contact', models.ForeignKey(orm['addressbook.contact'], null=False))
        ))
        db.create_unique('accessions_accession_sources', ['accession_id', 'contact_id'])

        # Adding model 'Location'
        db.create_table('accessions_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('shelf', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('accessions', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Accession'
        db.delete_table('accessions_accession')

        # Removing M2M table for field sources on 'Accession'
        db.delete_table('accessions_accession_sources')

        # Deleting model 'Location'
        db.delete_table('accessions_location')


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
        'accessions.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shelf': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        }
    }

    complete_apps = ['accessions']