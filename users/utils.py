from rest_framework.response import Response
import jwt
from django.conf import settings
from datetime import datetime, timedelta

def standard_response(data=None, message='Success', status=200):
    return Response({
        'data': data,
        'message': message
    }, status=status)


def generate_token(user):
    payload = {
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')

def decode_token(token):
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
