from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OrderList, Product
from django.views import generic


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
    order_list = OrderList.objects.filter(user=request.user)
    return render(request, 'personalAccount/cabinet.html', {'order_list': order_list})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def remove_from_cart(request):
    user = request.user
    product_id = request.POST.get('product_id')
    product = Product.objects.get(product_id=product_id)
    try:
        order_item = OrderList.objects.get(user=user, product=product)
        if order_item.count > 1:
            order_item.count -= 1
            order_item.save()
        else:
            order_item.delete()
    except OrderList.DoesNotExist:
        pass

    return redirect(request.META.get('HTTP_REFERER', 'cabinet'))


class OrderListView(generic.ListView):
    model = OrderList
    context_object_name = 'order_list'
