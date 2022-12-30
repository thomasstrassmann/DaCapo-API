from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer
from rest_framework import generics, permissions
from dacapo_api.permissions import IsOwnerOrReadOnly


class BookmarkList(generics.ListCreateAPIView):
    """
    Retrieve all bookmarks or get the opportunity to
    bookmark when authenticated.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Get access to bookmark and the option to delete it,
    if you are the owner.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
