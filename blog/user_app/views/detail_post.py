from django.views.generic.detail import DetailView
from user_app.models import Post

class DetailPost(DetailView):
    model = Post
    template_name = "user_app/detail_post.html"
    context_object_name = "post"