from django.urls import path

from .views import post_list_view, post_create_view

urlpatterns = [
    path('', post_list_view, name='home'),
    path('create/', post_create_view, name='create'),
]