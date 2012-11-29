from django.db import models
from addressbook.models import Contact
from locations.models import Location

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    string = models.CharField("Subject", max_length=100)

    @staticmethod
    def autocomplete_search_fields():
        return ('string__icontains',)

    def __unicode__(self):
        return self.string


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    call_no = models.CharField(max_length=7, blank=True)
    title = models.CharField(max_length=100)
    origination = models.CharField(max_length=100, blank=True)
    items = models.CharField(max_length=100, blank=True)
    lin_ft = models.CharField("Linear ft.", max_length=50, blank=True)
    date_start = models.CharField(max_length=10, blank=True)
    date_end = models.CharField(max_length=10, blank=True)
    abstract = models.TextField(blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    sources = models.ManyToManyField(Contact, blank=True)
    acc_restrict = models.TextField("Access restrictions", blank=True)
    use_restrict = models.TextField("Use restrictions", blank=True)
    notes = models.TextField(blank=True)
    processed = models.BooleanField()
    marc = models.BooleanField("MARC")
    umarmot = models.BooleanField("UMarmot")
    ead = models.BooleanField("EAD")
    inventory = models.BooleanField()
    locations = models.ManyToManyField(Location, blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return ('title__icontains',)

    def __unicode__(self):
        return self.title

