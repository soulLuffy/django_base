from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)  # 布尔值

    class Meta:
        db_table = 'BookInfo'  # 自定义数据表名称
        verbose_name = '书籍管理'  # admin站点使用
