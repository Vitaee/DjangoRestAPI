from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
	path('login/', views.user_login, name="list"),
	path('register/', views.user_register, name="list"),
	path('resetpass/',views.user_forget_pass, name='userFpass'),
	path('newpass/<str:key>/',views.user_new_pass, name='userNewpass')


]
