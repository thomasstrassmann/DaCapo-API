from rating.models import Rating
from django.db import IntegrityError
from rest_framework import serializers


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer of the Rating model.
    The create method handles duplicates (Integrity errors).
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    rated_user = serializers.ReadOnlyField(
        source='profile_id.owner.username')

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'owner_id', 'rated_user', 'profile_id',
                  'rating', 'created', 'updated']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'info': 'duplicate'
            })
