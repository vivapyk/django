from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
admin.site.unregister(Post)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
# admin.site.register(Post, PostAdmin)