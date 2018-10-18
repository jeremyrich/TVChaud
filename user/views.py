from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def user_details(request, user_id):

    output = {'user_id': user_id}

    return render(request, 'user/details.html', output)
