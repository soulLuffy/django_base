from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo, Characters


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

# -------------------------------查询的F对象------------------------------------
from django.db.models import F

# 用于2个属性的比较。 用法：以filter为例，objects.filter(属性名__运算符=F('第二个属性名'))
# 查询阅读量比评论数多的数据
BookInfo.objects.filter(read_count__gt=F('comment_count'))
# 查询评论数多于阅读量2倍的数据
BookInfo.objects.filter(comment_count__gt=F('read_count') * 2)

# --------------------------------查询的Q对象------------------------------------
# 1. and 查询  -- 查询阅读量小于40且id小于4的数据
BookInfo.objects.filter(read_count__lt=40).filter(id__lt=4)
BookInfo.objects.filter(read_count__lt=40, id__lt=4)

from django.db.models import Q

# 2. Q对象可用于and、or、not查询，主要用于or
# 2.1 or用法：BookInfo.objects.filter(Q(属性名__运算符=值) | Q(属性名__运算符=值) | ...)
# 2.2 and用法：BookInfo.objects.filter(Q(属性名__运算符=值) & Q(属性名__运算符=值) & ...)
# 2.3 not用法：BookInfo.objects.filter(~Q(属性名__运算符=值))

# or 查询 -- 阅读量小于30或者id大于3的数据
BookInfo.objects.filter(Q(read_count__lt=30) | Q(id__gt=3))
BookInfo.objects.filter(~Q(id=3))

# count()获取数量
BookInfo.objects.filter(id__lt=3).count()

# ---------------------------聚合函数 aggregate---------------------------------
from django.db.models import Sum, Max, Min, Avg, Count

BookInfo.objects.aggregate(Sum('read_count'))  # 结果为一个字典  {'read_count__sum': 126}

# ---------------------------排序---------------------------------
BookInfo.objects.all().order_by('comment_count')  # 默认为升序排序
BookInfo.objects.all().order_by('-comment_count')  # 降序排序  all()可以省略

# ---------------------------多表查询----------------------------------

# 1. 查询书籍id为1的所有人物信息
book = BookInfo.objects.get(id=1)
book.characters_set.all()

# 通过人物表查询
Characters.objects.filter(book=1)  # 这里的book为book_id

# 2. 查询人物为1的书籍信息
person = Characters.objects.get(id=1)  # 人物信息对象
# person.book --> 人物对应的书籍对象

# 通过从表查主表的信息
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(characters__name='郭靖')
# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(characters__description__contains='八')

# 通过主表差从表信息
# 查询书名为"天龙八部"的所有人物
Characters.objects.filter(book__name='天龙八部')
# 查询图书阅读量大于30的所有人物
Characters.objects.filter(book__read_count__gt=30)