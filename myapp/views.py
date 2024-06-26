from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, world!"})

from django.shortcuts import redirect
from django.http import JsonResponse
import requests

def callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    token_url = 'http://localhost:8000/o/token/'
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'http://localhost:8000/callback'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return JsonResponse(response.json())
    return JsonResponse(response.json(), status=response.status_code)


from django.http import HttpResponse
from django.core.management import call_command

def run_create_superuser(request):
    call_command('create_superuser')
    return HttpResponse('Superuser created')
