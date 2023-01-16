from rating.models import Rating
from rating.serializers import RatingSerializer
from rest_framework import generics, permissions, filters
from dacapo_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class RatingList(generics.ListCreateAPIView):
    """
    Retrieve all ratings or get the opportunity to rate when authenticated.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'owner__id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get access to rating and the option to update or delete it,
    if you are the owner.
    """
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rating.objects.all()
