from django.urls import path
from file import views


app_name = 'file'

urlpatterns = [
  path('read/', views.read_file, name='read_file'),
]