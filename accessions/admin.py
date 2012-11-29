from accessions.models import Accession
from locations.models import Location
from django.contrib import admin


class AccessionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
             'fields': ('number', 'title', 'call_no', 'date_rec', 'sources', 'collection', 'locations')
        }),
        ('Description', {
             'classes': ('grp-collapse grp-closed',),
             'fields': ('date_mat', 'desc', 'restrictions', 'lin_ft', 'boxes', 'items', 'condition')
        }),
        ('Accession data', {
             'classes': ('grp-collapse', 'grp-closed',),
             'fields': ('rec_by', 'rec_method', 'ack_date', 'value', 'accretion')
        }),
    )

    raw_id_fields = ('sources','collection','locations',)
    autocomplete_lookup_fields = {'m2m':['sources','collection', 'locations'],}
    list_display = ('title', 'number', 'date_rec')
    list_filter = ('date_rec', 'rec_by', 'call_no', 'sources')
    search_fields = ('title','number','desc','call_no','restrictions','rec_by', 'date_mat')


admin.site.register(Accession, AccessionAdmin)
  
    

