from .models import Instrument
from .serializers import InstrumentSerializer
from rest_framework import generics, permissions
from dacapo_api.permissions import IsOwnerOrReadOnly


class InstrumentList(generics.ListCreateAPIView):
    """
    This view lists all instruments and authenticated users can create a
    new item to sell.
    The method below (perform_create) binds the creator of an item as the owner
    to that entry.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view lists an individual instrument by its id.
    The view contains methods to get, update and delete an item, if the user
    is also the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.all()
