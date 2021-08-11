from django.shortcuts import render


def list(request):
    return render(request, 'frontend/list.html')


def user_login(request):
    return render(request, 'frontend/user_login.html')


def user_register(request):
    return render(request, 'frontend/user_register.html')


def user_forget_pass(request):
    return render(request, 'frontend/user_fpassword.html')


def user_new_pass(request, key):
    return render(request, 'frontend/newpass.html', {'key': key})
