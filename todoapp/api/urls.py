from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	path('user-login/', views.user_login, name="user-register"),
	path('user-register/', views.user_register, name="user-login"),
	path('current-user/', views.get_user, name='current-user'),
	path('user-logout/', views.user_logout),
	path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
