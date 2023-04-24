from django.urls import path
from book.views import add_book, shop, register, json
urlpatterns = [
    path('add/book/', add_book),
    # 把 url 路径中的参数写在 <> 中，可以通过视图函数接收，
    # 视图函数中形参的名字必须与<>中定义的参数名一致
    path('<city_id>/<shop_id>/', shop),
    path('register/', register),
    path('json/', json)
]