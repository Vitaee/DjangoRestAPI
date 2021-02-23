from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics

from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView

from .serializers import ProjectSerializer, UserSerializer, RegisterSerializer
from .models import Projects
from knox.models import AuthToken



# Create your views here.

"""
API Overview
"""


class login_view(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(login_view, self).post(request, format=None)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Projects.objects.all()
    serializer = ProjectSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Projects.objects.get(id=pk)
    serializer = ProjectSerializer(tasks)
    return Response(serializer.data)



@api_view(['POST'])
def taskCreate(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    task = Projects.objects.get(id = pk)
    serializer = ProjectSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Projects.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")


