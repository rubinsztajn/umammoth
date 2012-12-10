from locations.models import Location
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'room')
    list_filter = ('room',)
    search_fields = ('room','location','collection__title', 'accession__title')

admin.site.register(Location, LocationAdmin)

