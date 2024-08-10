from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests

User = get_user_model()

@api_view(['POST'])
def google_login(request):
    token = request.data.get('token')
    if not token:
        return Response({'error': 'No token provided'}, status=400)
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)        
        user_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name', '')        
        user, created = User.objects.get_or_create(
            username=email,
            defaults={'email': email, 'first_name': name}
        )
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    except ValueError as e:
        return Response({'error': f'Invalid token: {str(e)}'}, status=400)

# stepebi :
# id tokens damibrunebs da postis mere sccess-refreshs, mara id tokens ver vxedav :DD
