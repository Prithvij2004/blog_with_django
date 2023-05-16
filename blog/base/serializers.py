from rest_framework import serializers

from .models import Post
from likes_comments.models import Like


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "date_published", "date_updated", "likes_count"]
        read_only_fields = ['votes']

    def create(self, validated_data):
        """
        It is best to create the slug a string based on the title, content and some unique number.
        """
        validated_data['slug'] = validated_data['title']
        return super().create(validated_data)

    def get_likes_count(self, obj):
        return Like.objects.filter(post=obj).count()
