from celery import shared_task
import os

@shared_task
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except Exception as e:
        return f"Error processing file: {e}"