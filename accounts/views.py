from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'], first_name=data['first_name'],
                                     last_name=data['last_name'], password=data['password_2'])
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            return redirect('home:home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/user_register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'خوش آمدید', 'primary')
                return redirect('home:home')
            else:
                messages.error(request, 'نام کاربری یا کلمه عبور اشتباه است', 'danger')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', 'dark')
    return redirect('home:home')
