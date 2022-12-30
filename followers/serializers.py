from .models import Follower
from django.db import IntegrityError
from rest_framework import serializers


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for Follower.
    The create method makes sure, that it is not possible to
    follow the same user more than once.
    """
    following_username = serializers.ReadOnlyField(
        source='following_user.username')
    followed_username = serializers.ReadOnlyField(
        source='followed_user.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'following_username' 'created',
            'followed_user', 'followed_username'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'info': 'duplicate'})
