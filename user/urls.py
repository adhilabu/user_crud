from django.urls import path
from user.views import UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView

app_name = 'user'

urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
]
