from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    # return render(request, 'accounts/signup.html', {'form': form})
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    pass

def signout(request):
    logout(request)
    return redirect('login')

