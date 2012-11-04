from accessions.models import Accession
from locations.models import LocationMap
from django.contrib import admin

class LocationInline(admin.TabularInline):
    model = LocationMap
    fields = ('room', 'shelf')
    extra = 1
    

class AccessionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
             'fields': ('number', 'title', 'call_no', 'date_rec', 'sources', 'collection')
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

    raw_id_fields = ('sources','collection',)
    autocomplete_lookup_fields = {'m2m':['sources','collection'],}
    list_display = ('title', 'number', 'date_rec')
    list_filter = ('date_rec', 'rec_by', 'call_no')
    search_fields = ('title','desc','call_no','restrictions','rec_by')
    inlines = [LocationInline]

admin.site.register(Accession, AccessionAdmin)
  
    

