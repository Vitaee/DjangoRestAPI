from django.shortcuts import render

# Create your views here.

def list(request):
	return render(request, 'frontend/list.html')

def user_login(request):
	return render(request, 'frontend/user_login.html')

def user_register(request):
	return render(request, 'frontend/user_register.html')

