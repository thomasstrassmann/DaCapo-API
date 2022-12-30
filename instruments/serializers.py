from rest_framework import serializers
from instruments.models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(
        source='owner.profile.avatar.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Avatar larger than 2MB!')
        if value.image.height > 2048:
            raise serializers.ValidationError(
                'Avatar larger than 2048px!'
            )
        if value.image.width > 2048:
            raise serializers.ValidationError(
                'Avatar larger than 2048px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Instrument
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_avatar', 'created', 'updated',
            'title', 'description', 'image', 'price', 'category',
        ]
