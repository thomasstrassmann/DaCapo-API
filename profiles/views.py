from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics, filters
from dacapo_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    """
    List of all profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        instruments_count=Count('owner__instrument', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created')
    ordering_fields = [
        'instruments_count',
        'followers_count',
        'following_count',
        'owner__following__created',
        'owner__followed__created',
    ]
    filter_backends = [
        filters.OrderingFilter
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Authenticated owners can get and update their profile.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        instruments_count=Count('owner__instrument', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created')
