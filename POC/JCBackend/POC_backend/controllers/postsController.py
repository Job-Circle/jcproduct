from utils import db
from django.http import JsonResponse
import json
import requests

posts = db['posts']
access_token = 'YOUR_ACCESS_TOKEN'

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
        message="by "+post_data.get('author')+": "+ post_data.get('title')+"\n" +post_data.get('content')
        payload = {
                        'access_token': access_token,
                        'message': message
                    }
        posts.insert_one(post)
        url = 'https://graph.facebook.com/296731426868004/feed'
        response = requests.post(url, data=payload)
        print(response.json())
        return JsonResponse({'message': 'Post created successfully'}, status=201)
    return JsonResponse({'message': 'Invalid request'}, status=400)