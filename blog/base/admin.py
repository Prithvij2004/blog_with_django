from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'date_published', 'upvotes')
    list_filter = ('date_published',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slugs': ('title',)}

admin.site.register(Post)
    