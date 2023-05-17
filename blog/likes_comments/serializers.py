from rest_framework import serializers

from .models import Like
from .models import Comment


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ["id", "post", "user", "created_at"]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
