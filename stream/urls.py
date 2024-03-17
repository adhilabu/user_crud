from django.urls import path
from stream import views

app_name = 'stream'

urlpatterns = [
    path('', views.show_stream_sentence, name='show_stream_sentence'),
    path('stream/', views.stream_sentence, name='stream_sentence'),
]