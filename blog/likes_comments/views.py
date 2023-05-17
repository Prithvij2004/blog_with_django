from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from base.models import Post
from .models import Like
from .serializers import LikeSerializer


class LikeCreateView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        if Like.objects.filter(user=self.request.user, post=post).exists():
            raise ValidationError("You have already liked this post")
        serializer.save(user=self.request.user, post=post)


like_create_view = LikeCreateView.as_view()


class LikeDeleteView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return Like.objects.get(user=self.request.user, post_id=post_id)


like_delete_view = LikeDeleteView.as_view()
