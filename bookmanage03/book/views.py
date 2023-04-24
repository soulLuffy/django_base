from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo


# Create your views here.
def add_book(request):
    book = BookInfo(name='django', pub_date='2023-4-24', readcount=30)
    # book.save()
    return HttpResponse('添加成功')
