from django.shortcuts import render
from college.models import Post


def index(request):
    post = Post.objects.order_by('date')[:5]
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)
