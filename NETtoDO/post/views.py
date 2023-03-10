from django.shortcuts import render, redirect

from .forms import AddPostForm
from .models import Post, Days


def home_page(request):
    posts = Post.objects.all()
    days = Days.objects.all()
    return render(request,'post/index.html',{'posts' : posts, 'days' : days})


def show_day(request, day_id):
    posts = Post.objects.filter(day=day_id)
    return render(request, 'post/show.html', {'posts':posts})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddPostForm()
    return render(request,'post/add_post.html',{'form':form})