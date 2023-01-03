from rest_framework import serializers
from wanted.models import Wanted
from bookmarks.models import Bookmark


class WantedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(
        source='owner.profile.avatar.url')
    bookmark_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, wanted=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Wanted
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_avatar', 'created', 'updated',
            'title', 'description', 'category',
            'bookmark_id', 'bookmarks_count',
        ]
