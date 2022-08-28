from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.MainScreen.as_view(), name='index'),
    path('detail/<pk>', views.DetailPost.as_view(), name='detail'),
]