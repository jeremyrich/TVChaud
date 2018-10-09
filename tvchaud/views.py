from django.shortcuts import render
from series.forms import LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
