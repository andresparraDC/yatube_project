from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse('This is my HOME Saphiens!')

    # html_content = '<html><head><title>Yatube</title></head><body>'
    # html_content += '<h1>Главная страница</h1>'
    # html_content += '</body></html>'
    # return HttpResponse(html_content)

    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, pk):
    return HttpResponse(f'Posts from Group {pk}')
