from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import Post_Form


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = Post_Form()
    return render(request, 'blog/post_new.html', {'form' : form})
