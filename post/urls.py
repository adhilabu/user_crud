from django.urls import path
from post.views import PostListAPIView, PostFilterByTitleAPIView, PostRecentCommentsAPIView, PostByCreatedAtAPIView, PostDeleteAPIView

app_name = 'post'

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/filter/no-title/', PostFilterByTitleAPIView.as_view()),
    path('posts/recent-comments/', PostRecentCommentsAPIView.as_view()),
    path('posts/created-at/', PostByCreatedAtAPIView.as_view()),
    path('posts/<int:pk>/', PostDeleteAPIView.as_view()),
]
