from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {"form":form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'register/login.html', {'form': form, 'error': "Invalid username or password."})
    
    else:
        form = LoginForm(request.POST)
                
    return render(request, 'register/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')