from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostList(ListAPIView):
    queryset = Post.objects.all().order_by('-date_published')
    serializer_class = PostSerializer


post_list_view = PostList.as_view()


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_create_view = PostCreate.as_view()


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_detail_view = PostDetail.as_view()


class PostDelete(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


post_delete_view = PostDelete.as_view()


class PostUpdate(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


post_edit_view = PostUpdate.as_view()

