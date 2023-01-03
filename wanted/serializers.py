from rest_framework import serializers
from wanted.models import Wanted


class WantedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(
        source='owner.profile.avatar.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Wanted
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_avatar', 'created', 'updated',
            'title', 'description', 'category',
        ]
