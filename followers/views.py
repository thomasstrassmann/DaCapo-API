from .models import Follower
from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from dacapo_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    """
    The Follower list view retrieves all following users of
    another user. To follow, you must be authorized.
    The perform_create method binds the logged in user to the
    'following side'.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve / detroy view, as we can only follow or
    unfollow a user.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
