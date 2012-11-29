from django.contrib import admin
from django.forms.models import ModelForm
from umarmot.models import Subject, Collection


class CollectionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
                'fields': ('title','call_no','items','lin_ft','origination',('date_start','date_end'), 'locations')
        }),
        ('Abstract', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('abstract',)
        }),
        ('Administrative', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('sources', 'acc_restrict', 'use_restrict', 'notes')
        }),
        ('Collection status', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('processed','marc','umarmot','ead','inventory')
        }),
    )

    search_fields = ('title', 'abstract', 'call_no', 'origination')
    list_display = ('title', 'call_no')
    raw_id_fields = ('sources','locations',)
    autocomplete_lookup_fields = {
        'm2m':['sources', 'locations'],
    }




    def get_accessions(self, Collection):
        accs = Collection.accession_set.all()
        return accs

admin.site.register(Collection, CollectionAdmin)

