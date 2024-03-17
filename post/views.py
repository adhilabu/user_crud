from rest_framework import generics, filters
from django.db.models import Count
from django.db.models import Q
from post.models import PostModel, CommentModel
from post.serializers import PostSerializer
from rest_framework import serializers

class PostListAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all().annotate(comment_count=Count('commentmodel'))
    serializer_class = PostSerializer

class PostFilterByTitleAPIView(generics.ListAPIView):
    post_model_q = Q(title__isnull=True) | Q(title='')
    queryset = PostModel.objects.filter(post_model_q)
    serializer_class = PostSerializer

class PostRecentCommentsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.annotate(comment_count=Count('commentmodel')).order_by('-commentmodel__publication_date')
    serializer_class = PostSerializer

class PostByCreatedAtAPIView(generics.ListAPIView):
    queryset = PostModel.objects.order_by('-created_at')
    serializer_class = PostSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        comment_count = CommentModel.objects.filter(post=instance).count()
        if comment_count == 0:
            instance.delete()
        else:
            raise serializers.ValidationError("Cannot delete post with comments")
