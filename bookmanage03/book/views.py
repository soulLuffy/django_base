from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo


def add_book(request):
    book = BookInfo(name='django', pub_date='2023-4-24', readcount=30)
    # book.save()
    return HttpResponse('添加成功')


"""
-- 查询字符串
url以 ? 为分隔，前面为路径，后面为查询字符串
    -- ?key1=value1&key2=value2...
"""


def shop(request, city_id, mobile):
    print(city_id, mobile)
    """
      request.GET 可以获取 url 中的查询字符串参数
      得到的结果为一个QueryDict对象，类似字典，但可以一键多值
      print(query_params)  <QueryDict: {'order': ['readcount', 'commentcount'], 'id': ['1']}>
    """
    query_params = request.GET
    # 通过get()或索引可以获取一个值，如果一个键对应多个值，需要用getlist()方法获取
    num1 = query_params.get('id')
    num2 = query_params['id']
    # order = query_params['order']
    order = query_params.getlist('order')
    # print(num2, '\n', order)

    return HttpResponse('ok')


def register(request):
    # 通过form表单提交的数据
    data = request.POST
    print(data)  # <QueryDict: {'username': ['itcast'], 'password': ['123456']}>
    return HttpResponse('ok')


def json(request):
    # 通过request.body接收post请求发送的json数据
    body = request.body  # body为二进制数据
    # print(body)  # b'{\r\n    "username": "itcast",\r\n    "password": "123456",\r\n    "age": 20\r\n}'
    body_str = body.decode()  # json字符串
    # print(body_str)
    import json
    body_dict = json.loads(body_str)
    # print(body_dict)  # {'username': 'itcast', 'password': '123456', 'age': 20}

    # 请求头
    # print(request.META)
    print(request.META['SERVER_PORT'])

    # 获取请求方法
    print(request.method)
    return HttpResponse('json')
