from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
	path('login/', views.user_login, name="list"),
	path('register/', views.user_register, name="list"),


]
