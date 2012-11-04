from addressbook.models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'notes']

admin.site.register(Contact, ContactAdmin)
