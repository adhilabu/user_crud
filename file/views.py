from file.utils import count_words_in_file
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
@csrf_exempt
def read_file(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      file_path = data.get('file_path')
      if file_path:
        file_path = 'D:\projects\ailasya\task_1\task_1\sample.txt'
        word_count_task = count_words_in_file.apply_async(args=[file_path])
        count = word_count_task.get()
        response_data = {'message': f"Number of words is {count}!"}
        return JsonResponse(response_data, status=200) 
      else:
        message = "Error: Missing 'file_path' in JSON request."
        return JsonResponse({'message': message}, status=400) 
    except json.JSONDecodeError:
      message = "Error: Invalid JSON request."
      return JsonResponse({'message': message}, status=400) 
  else:
    return JsonResponse({'message': 'Use POST request with JSON data'}, status=405)  # Method Not Allowed
