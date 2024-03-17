from rest_framework import serializers
from .models import PostModel, CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'publication_date')

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ('id', 'title', 'author', 'created_at', 'comment_count')

    def get_comment_count(self, obj):
        return CommentModel.objects.filter(post_id=obj.id).count()
