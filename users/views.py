from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import CustomUser
from .utils import generate_token, Response
from .authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

class RegisterView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    parser_classes = (MultiPartParser, FormParser)  # Add parsers to handle FormData

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'Username or password not provided.'}, status=400)

        user = CustomUser.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        token = generate_token(user)
        response = Response({
            'message': 'success!',
            'jwt': token,
            'user_type': 'admin' if user.is_superuser else 'manager'
        })
        response.set_cookie(key='jwt', value=token, httponly=True, secure=True, samesite='Lax')
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response({'message': 'Logged out successfully'})
        response.delete_cookie('jwt')
        return response

class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , IsAdminUser]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class DeleteUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def delete(self, request, id):
        
        try:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=204)
        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

class SingleUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response({'user': serializer.data})
        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

class ModifyUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def put(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

