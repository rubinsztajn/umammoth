from django.db import models
from accessions.models import Accession
from umarmot.models import Collection

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class LocationMap(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room)
    shelf = models.CharField(max_length=20)
    accession = models.ForeignKey(Accession, null=True)
    collection = models.ForeignKey(Collection, null=True)

    def __unicode__(self):
        return "%s %s" % (self.room, self.shelf)

    class Meta:
        verbose_name = 'location'

    

