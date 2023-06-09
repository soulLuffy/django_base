from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)  # 布尔值

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'BookInfo'  # 自定义数据表名称
        verbose_name = '书籍管理'  # admin站点使用

    # Characters表与此表关联，系统会自动生成一个属性
    # characters_set = [人物信息]  获取属性时用
    # characters                  查询时可使用

class Characters(models.Model):
    name = models.CharField(max_length=20, unique=True)
    gender_choices = (
        (1, 'male'),
        (2, 'female')
    )
    gender = models.SmallIntegerField(choices=gender_choices, default=1)
    description = models.CharField(max_length=255, null=True)
    is_delete = models.BooleanField(default=False)
    # 外键  系统会自动为外键的属性名添加 _id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'characters'

    def __str__(self):
        return self.name
