from django.contrib import admin
from .models import Post, Comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierachy = 'publish'
    list_filter = ('status', 'created_on')
    # ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)   


admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email address', 'body']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)
