from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout as logout_view
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('catalog')
    return render(request, 'personalAccount/login.html')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            user = User.objects.create_user(username=username, password=password)
            user_login(request, user)
            return redirect('catalog')
    return render(request, 'personalAccount/registration.html')


def cabinet(request):
    return render(request, 'personalAccount/cabinet.html')


def logout_view(request):
    return render(request, 'personalAccount/logout.html')
