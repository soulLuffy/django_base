from django.urls import path
from book.views import add_book, shop, register, json
from django.urls import converters
from django.urls import register_converter


# 1. 自定义转换器
class MobileConverter:
    # 转换器验证的核心为正则
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


# 2. 先注册转换器，再使用
# 参数1：converter --> 自定义的转换器类
# 参数2：type_name --> 转换器名字
register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('add/book/', add_book),
    # 把 url 路径中的参数写在 <> 中，可以通过视图函数接收，
    # 视图函数中形参的名字必须与<>中定义的参数名一致

    # <转换器名字:变量名>
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json)
]
