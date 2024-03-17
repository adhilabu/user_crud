from django.contrib import admin
from post.models import PostModel, CommentModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'get_comment_count') 
    readonly_fields = ('get_comment_count',) 

    def get_comment_count(self, obj): 
        return CommentModel.objects.filter(post=obj).count()

    get_comment_count.short_description = 'Comment Count' 


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment', 'publication_date')
    list_filter = ('post',) 
