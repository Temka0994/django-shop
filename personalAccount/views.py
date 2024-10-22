from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('catalog')
        else:
            messages.error(request, "Неправильні або не дійсні дані")
    return render(request, 'personalAccount/login.html')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Користувач з таким логіном вже існує")
        elif password == password_confirmation:
            user = User.objects.create_user(username=username, password=password)
            user_login(request, user)
            return redirect('catalog')
        else:
            messages.error(request, "Виникла помилка, перевірте правильність введених даних")
    return render(request, 'personalAccount/registration.html')


@login_required
def cabinet(request):
    return render(request, 'personalAccount/cabinet.html')


def logout_view(request):
    logout(request)
    return redirect('home')
