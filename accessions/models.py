from django.db import models
from addressbook.models import Contact
from locations.models import Location
from umarmot.models import Collection


class Accession(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)
    title = models.TextField()
    call_no = models.CharField(max_length=100, blank=True)
    collection = models.ManyToManyField(Collection, blank=True)
    date_rec = models.DateField("Date recieved")
    date_mat = models.CharField("Date(s)",max_length=100, blank=True)
    desc = models.TextField("Description", blank=True)
    restrictions = models.TextField(blank=True)
    lin_ft = models.CharField("Linear feet",max_length=100, blank=True)
    boxes = models.CharField("Boxes", max_length=100, blank=True)
    items = models.CharField("Items", max_length=100, blank=True)
    condition = models.TextField(blank=True)
    rec_by = models.CharField("Received by", max_length=100, blank=True)
    rec_method = models.CharField("Method received", max_length=100, blank=True)
    ack_date = models.CharField("Date acknowledged", max_length=100, blank=True)
    value = models.CharField(max_length=100, blank=True)
    accretion = models.BooleanField()
    sources = models.ManyToManyField(Contact, blank=True)
    locations = models.ManyToManyField(Location, blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return ('number__icontains',)

    def __unicode__(self):
        return self.number

