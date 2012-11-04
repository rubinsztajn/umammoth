from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from umarmot.models import Collection

class SourceLookup(LookupChannel):
    model = Collection
    
    def get_query(self, q, request):
        return Collection.objects.filter(Q(sources__first_name__icontains=q) | Q(sources__last_name__icontains=q)).order_by('last_name')

    def get_result(self, obj):
        return obj.name

    
