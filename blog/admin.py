from django.contrib import admin
from .models import Post, Comment



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author','publish', 'status']
    search_fields = ['title', 'body'] #define searchable fields
    list_filter = ['status', 'created', 'publish', 'author'] #to filter results by fields
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish' #for nav links to navigate through a date hierarchy
    ordering = ['status', 'publish']# to order the posts by status and publish


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
