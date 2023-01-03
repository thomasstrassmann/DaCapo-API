from .models import Wanted
from .serializers import WantedSerializer
from rest_framework import generics, permissions, filters
from dacapo_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class WantedList(generics.ListCreateAPIView):
    """
    This view lists all requests of users and authenticated users can create a
    new entry.
    The method below (perform_create) binds the creator of an item as the owner
    to that entry.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WantedSerializer
    queryset = Wanted.objects.annotate(
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created')

    ordering_fields = [
        'bookmarks_count',
        'bookmarks__created',
    ]

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter
    ]

    filterset_fields = [
        'category',
        'owner__followed__owner__profile',
        'bookmarks__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WantedDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view lists an individual request by its id.
    The view contains methods to get, update and delete an item, if the user
    is also the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WantedSerializer
    queryset = Wanted.objects.annotate(
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created')
