from django.contrib import admin
from django.forms.models import ModelForm
from umarmot.models import Collection
from locations.models import LocationMap


class LocationInline(admin.TabularInline):
    model = LocationMap
    fields = ('room', 'shelf',)
    extra = 1

class CollectionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
                'fields': ('title','call_no','items','lin_ft','origination',('date_start','date_end'))
        }),
        ('Abstract', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('abstract',)
        }),
        ('Sources', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('sources',)
        }),
        ('Collection status', {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('processed','marc','umarmot','ead','inventory')
        }),
    )

    search_fields = ('title', 'abstract', 'accs', 'call_no', 'origination')
    list_display = ('title', 'call_no')
    raw_id_fields = ('sources',)
    autocomplete_lookup_fields = {
        'm2m':['sources'],
    }



    def get_accessions(self, Collection):
        accs = Collection.accession_set.all()
        return accs

    inlines = [LocationInline]


admin.site.register(Collection, CollectionAdmin)

