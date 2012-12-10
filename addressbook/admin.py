from addressbook.models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'notes']
    list_display = ['last_name', 'first_name', 'address1', 'city', 'state']

admin.site.register(Contact, ContactAdmin)
