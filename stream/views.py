from django.http import StreamingHttpResponse
from django.shortcuts import render
import random

def show_stream_sentence(request):
    return render(request, 'templates/stream.html')

def stream_sentence(request):
  words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
  sentence = " ".join(random.choices(words, k=5))
  def generate_chunks():
    for word in sentence.split():
      yield f"{word} "
      # Simulate a slight delay between words
    #   yield from (.1,)
  return StreamingHttpResponse(generate_chunks(), content_type="text/plain")
