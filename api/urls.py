from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	path('user-login/', views.UserLoginView.as_view(), name="user-register"),
	path('user-register/', views.UserRegisterView.as_view(), name="user-login"),
	path('current-user/', views.GetUserView.as_view(), name='current-user'),
	path('user-logout/', views.UserLogoutView.as_view()),
	path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
