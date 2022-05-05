from django.shortcuts import render, get_object_or_404
from .models import Post, Group


app_name = 'posts'


def index(request):
    title = 'Главная страница сообщений'
    num_posts = 10
    posts = Post.objects.order_by('-pub_date')[:num_posts]
    template = 'posts/index.html'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    num_posts = 10
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:num_posts]
    template = 'posts/group_list.html'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
