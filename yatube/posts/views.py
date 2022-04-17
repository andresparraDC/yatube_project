from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('This is my HOME Saphiens!')


def group_posts(request, pk):
    return HttpResponse(f'Posts from Group {pk}')
