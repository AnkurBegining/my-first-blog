from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})