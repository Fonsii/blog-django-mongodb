from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainScreen.as_view(), name='index'),
    path('detail/<pk>', views.DetailPost.as_view(), name='detail'),
]