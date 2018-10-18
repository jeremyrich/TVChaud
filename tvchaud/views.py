from django.shortcuts import render
from user.forms import LoginForm

from dbtables.User import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# login page
def mylogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            message = 'logging in'
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())


# logout redirect
def mylogout(request):
    logout(request)
    return render(request, 'login.html')


# create user
def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                return render(request, 'register.html', {'error': True, 'form': form})

            new_user = User(first_name, last_name, email)
            new_user.set_password(make_password(password))

            new_user.insert()

            return render(request, 'login.html')
    else:
        form = LoginForm()
        return render(request, 'register.html', {'form': form})
