from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import EngineerSerializer
from .models import Engineer
from users.authentication import JWTAuthentication

class AddEngineerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EngineerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DeleteEngineerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            engineer = Engineer.objects.get(pk=pk)
            engineer.delete()
            return Response(status=204)
        except Engineer.DoesNotExist:
            return Response({'detail': 'Engineer not found.'}, status=404)

class ViewAllEngineersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        engineers = Engineer.objects.all()
        serializer = EngineerSerializer(engineers, many=True)
        return Response(serializer.data)

class ViewEngineerDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            engineer = Engineer.objects.get(pk=pk)
            serializer = EngineerSerializer(engineer)
            return Response(serializer.data)
        except Engineer.DoesNotExist:
            return Response({'detail': 'Engineer not found.'}, status=404)

class ModifyEngineerDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            engineer = Engineer.objects.get(pk=pk)
            serializer = EngineerSerializer(engineer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Engineer.DoesNotExist:
            return Response({'detail': 'Engineer not found.'}, status=404)
