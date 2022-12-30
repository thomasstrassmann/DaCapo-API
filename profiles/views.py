from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics
from dacapo_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List of all profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Authenticated owners can get and update their profile.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
