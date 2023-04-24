from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo


def index(request):
    return render(request, 'books/index.html')


# ------------------------------增加数据-----------------------------------

# 方法一：
# 创建一个 BookInfo 实例对象
book = BookInfo(name='django', pub_date='2023-4-24', read_count=20)
# 调用save()方法保存数据
book.save()

# 方法二：
# objects 相当于一个代理，可以完成增删改查操作
BookInfo.objects.create(name='管理部门', pub_date='2022-5-10', read_count=100)

# -------------------------------修改数据-----------------------------------

# 方式一：
book = BookInfo.objects.get(id=6)  # 获取ID为6的数据对象
book.name = '运维部门'
book.save()

# 方式二:
BookInfo.objects.filter(id=6).update(name='爬虫入门', comment_count=60)

# BookInfo.objects.get(id=5).update(comment_count=56)  ps: 通过objects.get获取到的数据对象没有update方法

# -------------------------------删除数据-------------------------------------

# 方式一：
book = BookInfo.objects.get(id=6)
book.delete()

# 方式二：
BookInfo.objects.get(id=7).delete()
BookInfo.objects.filter(id=5).delete()

# ------------------------------查询数据-----------------------------------------
"""
    # 查询数据的几种方法：get、filter、exclude
    # objects().all()  --> 获取所有数据，结果为一个列表
    # 1. get获取到的是一个符合条件的数据对象，如果找不到会报错,符合条件的不止一个也会报错
    try:
        book = BookInfo.objects.get(id=6)
    except BookInfo.DoesNotExist:
        print('数据不存在')
    
    # 2. filter获取到的是符合条件的对象列表
    books = BookInfo.objects.filter(id=4)
    
    # pk 为主键
    book = BookInfo.objects.get(pk=4)
"""

# 1. contains 包含 --查询名字包含湖的书籍
BookInfo.objects.filter(name__contains='湖')

# 2. endswith 以xx结尾 --查询以传结尾的书籍
BookInfo.objects.filter(name__endswith='传')

# 3. isnull 是否为空 --查询书名为空的数据
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(name__isnull=False)

# 4. in 范围查询 --查询ID为1、3、5的书籍
BookInfo.objects.filter(id__in=[1, 3, 5])

# 5. 比较运算符
"""
    gt  大于
    gte 大于等于
    
    lt  小于
    lte 小于等于
"""
BookInfo.objects.filter(id__gt=3)
BookInfo.objects.filter(id__gte=3)

# 6. 时间查询  --日期格式为 'YYYY-MM-DD'
# 6.1 查询1980年发表的书籍 __year 年份
BookInfo.objects.filter(pub_date__year='1980')
# 6.2 查询1980年1月1日之后发表的数据
BookInfo.objects.filter(pub_date__gt='1980-1-1')