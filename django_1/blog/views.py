from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/main.html', {'posts':posts})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# request를 받아 render 메서드 호출 & render의 리턴값('blog/post_list.html' 템플릿)을 반환
