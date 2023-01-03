from rating.models import Rating
from rating.serializers import RatingSerializer
from rest_framework import generics, permissions
from dacapo_api.permissions import IsOwnerOrReadOnly


class RatingList(generics.ListCreateAPIView):
    """
    Retrieve all ratings or get the opportunity to rate when authenticated.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

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
