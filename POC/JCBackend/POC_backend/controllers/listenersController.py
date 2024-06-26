from utils import db
from django.http import JsonResponse
import json

listeners = db['listeners']

def Addlistener(request):
    if request.method == 'POST':
        listener_data = json.loads(request.body.decode('utf-8'))
        listener = {
            'groupId': listener_data.get('groupId'),
        }
        listeners.insert_one(listener)
        return JsonResponse({'message': 'New group created successfully'}, status=201)
    return JsonResponse({'message': 'Invalid request'}, status=400)