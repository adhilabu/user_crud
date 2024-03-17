from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from user.models import UserProfile
from user.serializers import UserProfileSerializer
from user.pagination import CustomUserPagination


class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['name']
    ordering = ['name']
    pagination_class = CustomUserPagination
    
class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer