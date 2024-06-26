from utils import db
from django.http import JsonResponse
import json

posts = db['posts']

def createPosts(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode('utf-8'))
        post = {
            'title': post_data.get('title'),
            'content': post_data.get('content'),
            'author': post_data.get('author'),
            'date': post_data.get('date'),
            'likes': 0,
            'dislies': 0,
        }
        posts.insert_one(post)
        return JsonResponse({'message': 'Post created successfully'}, status=201)
    return JsonResponse({'message': 'Invalid request'}, status=400)