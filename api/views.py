from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, TaskRegisterSerializer, UserSerializer, UserRegisterSerializer
from .models import Task, User
import jwt, datetime
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

class UserLoginView(APIView):

    @method_decorator(csrf_exempt)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = get_user_model().objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response


class UserRegisterView(APIView):

    def post(self, request):
        js_data = request.data
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        payload = {
            'email': js_data['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response


class UserLogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


class GetUserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('You are not logged in! Or Token Expired Log in again.')

        try:
            payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('En error!')

        user = get_user_model().objects.filter(email=payload['email']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskRegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

    user = User.objects.get(email=payload['email'])

    try:
        task = Task.objects.get(id=pk,created_by=user.username)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except Exception as err:
        return Response({'msg': 'You do not have access to this item!'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['DELETE'])
def taskDelete(request, pk):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

    user = User.objects.get(email=payload['email'])

    try:
        task = Task.objects.get(id=pk, created_by=user.username)
        task.delete()
        return Response({'msg': 'Item deleted successfully'}, status=status.HTTP_200_OK)

    except Exception as err:
        return Response({'msg': 'You do not have access to this item!'}, status=status.HTTP_403_FORBIDDEN)
