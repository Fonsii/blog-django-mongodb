from django.views import generic
from django.shortcuts import render
from django.views.generic.list import ListView
from user_app.models import Post

class MainScreen(ListView):

    model = Post
    template_name = "user_app/index.html"
    context_object_name = "context"
    paginate_by = 5  # if pagination is desired
