from rest_framwork import generics, filters, permissons
from .models import Instruments
from .serializers import InstrumentSerializer
from dacapo_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class InstrumentList(generics.ListCreateAPIView):
    """
    This view lists all instruments and authenticated users can create a 
    new item to sell. 
    The method below (perform_create) binds the creator of an item as the owner
    to that entry.
    """


