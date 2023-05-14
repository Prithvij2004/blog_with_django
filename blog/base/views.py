from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Post
from .serializers import PostSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all().order_by('-date_published')
    serializer_class = PostSerializer


post_list_view = PostList.as_view()


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_create_view = PostCreate.as_view()
