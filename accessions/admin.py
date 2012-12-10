from accessions.models import Accession
from locations.models import Location
from django.contrib import admin


class AccessionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
             'fields': (('number','date_rec'),'accretion', 'title', 'date_mat', 'desc', 'call_no', 'sources', 'collection', 'locations')
        }),
        ('Administrative', {
             'classes': ('grp-collapse grp-closed',),
             'fields': ('restrictions', ('lin_ft', 'boxes', 'items'), 'condition', 'rec_by','value','admin_notes')
        }),
    )

    raw_id_fields = ('sources','collection','locations',)
    autocomplete_lookup_fields = {'m2m':['sources','collection', 'locations'],}
    list_display = ('number','title', 'date_rec')
    list_filter = ('date_rec', 'rec_by', 'call_no', 'sources')
    search_fields = ('title','number','desc','call_no','restrictions','rec_by', 'date_mat', 'admin_notes', 'sources__first_name', 'sources__last_name', 'collection__title', 'locations__location')


admin.site.register(Accession, AccessionAdmin)
  
    

