from django.db import models

class Location(models.Model):
    ROOMS = (
        (u'25',u'25'),
        (u'24',u'24'),
    )

    id = models.AutoField(primary_key=True)
    room = models.CharField(max_length=50, choices=ROOMS, blank=True)
    location = models.CharField(max_length=100)

    @staticmethod
    def autocomplete_search_fields():
        return ('location__icontains',)

    def __unicode__(self):
        return self.location


    

