from django.urls import path
from knox import views as knox_views
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('login/',views.login_view.as_view(), name="login"),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('logout/', knox_views.LogoutAllView.as_view(), name='logout'),



    #path('token-auth/', obtain_auth_token, name='api_token_auth'),
    
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]