from django.contrib import admin

from .models import Like
from .models import Comment


admin.site.register(Like)
admin.site.register(Comment)
