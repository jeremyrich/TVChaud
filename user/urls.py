"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.user_details, name='user_details'),

    # ajax calls for favorites
    url(r'^ajax/add_to_favorites/$', views.ajax_add_favorite, name="ajax_add_favorite"),
    url(r'^ajax/remove_from_favorites/$', views.ajax_remove_favorite, name="ajax_remove_favorite"),

    # ajax calls for friend requests
    url(r'^ajax/send_friend_request/$', views.ajax_send_friend_request, name="ajax_send_friend_request"),
    url(r'^ajax/accept_friend_request/$', views.ajax_accept_friend_request, name="ajax_accept_friend_request"),
    url(r'^ajax/decline_friend_request/$', views.ajax_decline_friend_request, name="ajax_decline_friend_request"),
]
