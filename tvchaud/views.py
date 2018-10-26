from django.shortcuts import render, redirect

from dbtables.User import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# login page
def mylogin(request):
    if request.method == 'POST':
        pass

    else:
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['class'] = 'form-control login-div login-field'
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['password'].widget.attrs['class'] = 'form-control login-div login-field'
        form.fields['password'].widget.attrs['placeholder'] = 'Password'

    return render(request, 'login.html', locals())


# logout redirect
def mylogout(request):
    logout(request)
    return redirect('login')


# create user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
