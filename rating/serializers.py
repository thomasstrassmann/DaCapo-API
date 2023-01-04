from rating.models import Rating
from django.db import IntegrityError
from rest_framework import serializers


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer of the Rating model.
    The create method handles duplicates (Integrity errors).
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    rated_user = serializers.ReadOnlyField(
        source='profile.owner.username')

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'profile', 'rated_user', 'rating',
                  'created', 'updated']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'info': 'duplicate'
            })
