from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Post)
admin.site.unregister(Post)


@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content_size', 'status', 'created_at', 'updated_at']
# admin.site.register(Post, PostAdmin)
    actions = ['make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'
    #content_size.allow_tags = True

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정포스팅을 published 상태로 변경'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
