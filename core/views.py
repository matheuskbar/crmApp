from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
        else:
            messages.error(request, 'Usuário ou Senha não correspondem. Por favor tente novamente!')
        return redirect('index')
    return render(request, 'login.html')


def logout(request):
    django_logout(request)
    return redirect('login')
