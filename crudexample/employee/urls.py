
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('add-user', views.add_user),
    path('update-user', views.update_user),
    path('delete-user', views.delete_user),
    path('get-user', views.get_user_details),
]