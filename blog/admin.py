from django.contrib import admin
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class AdminPosts(admin.ModelAdmin):
  list_display = ['title', 'published_date']