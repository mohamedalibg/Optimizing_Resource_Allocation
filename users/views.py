from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import CustomUser
import jwt, datetime
from django.core.exceptions import ObjectDoesNotExist
# Create your views here
class RegisterView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except KeyError:
            return Response({'detail': 'Invalid request. Missing username or password.'}, status=400)

        user = CustomUser.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response({
            'message': 'success!',
            'jwt': token
        })

        response.set_cookie(key='jwt', value=token, httponly=True)
        return response
class LogoutView(APIView):
    def post(self, request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'

        }
        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            users = CustomUser.objects.all()  
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)       
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Authentication credentials have expired.'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'detail': 'Invalid authentication token.'}, status=401)
    
class DeleteUserView(APIView):
    def delete(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = request.data.get('id')
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=204)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Authentication credentials have expired.'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'detail': 'Invalid authentication token.'}, status=401)
        
class ModifyUserView(APIView):
    def put(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = request.data.get('id')



        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Authentication credentials have expired.'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'detail': 'Invalid authentication token.'}, status=401)

