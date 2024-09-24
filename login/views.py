from django.db.transaction import commit
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from . import forms
from django.contrib.auth import logout


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect('/login')

        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login/login.html')


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.RegisterForm()
        return render(request, 'login/register.html', {
            'form': form
        })

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'login/register.html', {
                'form': form
            })

def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')