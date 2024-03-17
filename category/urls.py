from django.urls import path
from category.views import CategoryListAPIView

app_name = 'category'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
]