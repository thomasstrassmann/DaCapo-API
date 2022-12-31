from .models import Instrument
from .serializers import InstrumentSerializer
from rest_framework import generics, permissions, filters
from dacapo_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class InstrumentList(generics.ListCreateAPIView):
    """
    This view lists all instruments and authenticated users can create a
    new item to sell.
    The method below (perform_create) binds the creator of an item as the owner
    to that entry.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.annotate(
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created')

    ordering_fields = [
        'bookmarks_count',
        'bookmarks__created',
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

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
    queryset = Instrument.objects.annotate(
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created')
