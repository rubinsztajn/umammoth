from django.contrib import admin
from django.forms.models import ModelForm
from umarmot.models import Subject, Collection


class CollectionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
                'fields': (('call_no', 'coll_type'), 'locations','title','origination',('items','lin_ft'),('date_start','date_end'),'abstract')
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

    search_fields = ('title', 'abstract', 'call_no', 'origination', 'locations__location', 'date_start', 'date_end', 'accession__title')
    list_display = ('call_no', 'title', 'date_start', 'date_end', 'lin_ft')
    list_display_links = ('title',)
    list_filter = ('coll_type', 'umarmot', 'ead')
    raw_id_fields = ('sources','locations',)
    autocomplete_lookup_fields = {
        'm2m':['sources', 'locations'],
    }


admin.site.register(Collection, CollectionAdmin)

