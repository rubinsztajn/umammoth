from django.db import models
from django.contrib.localflavor.us.us_states import US_STATES

class Contact(models.Model):
    TITLES = (
        (u'Dr.', u'Dr.'),
        (u'Mr.', u'Mr.'),
        (u'Ms.', u'Ms.'),
        (u'Mrs.', u'Mrs.'),
        (u'Brig. Gen', u'Brig. Gen.'),
        (u'Dr. and Mrs.', u'Dr. and Mrs.'),
        (u'Mr. and Mrs.', u'Mr. and Mrs.'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, choices=TITLES, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    mi = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    address3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, choices=US_STATES, blank=True)
    zip = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    phone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    grad_class = models.CharField(max_length=200, blank=True)

    @staticmethod
    def autocomplete_search_fields():
        return ('first_name__icontains', 'last_name__icontains',)

    def __unicode__(self):
        return "%s %s %s %s" % (self.title, self.first_name, self.mi, self.last_name)

