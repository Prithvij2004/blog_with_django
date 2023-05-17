from rest_framework import serializers

from .models import Post
from likes_comments.models import Like, Comment
from likes_comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        """
        It is best to create the slug a string based on the title, content and some unique number.
        """
        validated_data['slug'] = validated_data['title']
        return super().create(validated_data)

    @staticmethod
    def get_likes_count(obj):
        return Like.objects.filter(post=obj).count()

    @staticmethod
    def get_comment_count(obj):
        return Comment.objects.filter(post=obj).count()


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
