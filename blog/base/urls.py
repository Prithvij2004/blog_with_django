from django.urls import path

from .views import (
    post_list_view,
    post_create_view,
    post_detail_view,
    post_delete_view,
    post_edit_view
)

urlpatterns = [
    path('', post_list_view, name='home'),
    path('create/', post_create_view, name='create'),
    path('<int:pk>/', post_detail_view, name='detail'),
    path('<int:pk>/delete/', post_delete_view, name='delete'),
    path('<int:pk>/edit/', post_edit_view, name='edit'),
]
