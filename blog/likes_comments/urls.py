from django.urls import path

from .views import (
    like_create_view,
    like_delete_view,
    comment_create_view,
    comment_delete_view
)


urlpatterns = [
    path('<int:post_id>/like/', like_create_view, name='like-create'),
    path('<int:post_id>/comment/', comment_create_view, name='comment-create'),
    path('<int:post_id>/like/delete/', like_delete_view, name='like-delete'),
    path('<int:post_id>/comment/<int:comment_id>/delete/', comment_delete_view, name='comment-delete'),
]
