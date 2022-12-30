from bookmarks.models import Bookmark
from django.db import IntegrityError
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer of the Bookmark model.
    The create method handles duplicates (Integrity errors).
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'instrument', 'created']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'info': 'duplicate'
            })
