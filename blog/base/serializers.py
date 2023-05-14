from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['slug', 'votes']

    def create(self, validated_data):
        """
        It is best to create the slug a string based on the title, content and some unique number.
        """
        validated_data['slug'] = validated_data['title']
        return super().create(validated_data)
