from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        "name": '马上双11，点我有惊喜'
    }
    return render(request, 'books/index.html', context)
