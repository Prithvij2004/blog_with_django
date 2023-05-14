from django.urls import path

from .views import (
    post_list_view,
    post_create_view,
    post_detail_view,
    post_delete_view
)

urlpatterns = [
    path('', post_list_view, name='home'),
    path('create/', post_create_view, name='create'),
    path('<slug:slug>/', post_detail_view, name='detail'),
    path('<slug:slug>/delete/', post_delete_view),
]
