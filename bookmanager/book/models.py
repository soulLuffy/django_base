from django.db import models


class BookInfo(models.Model):
    """图书信息表"""
    name = models.CharField(max_length=20)


class PeopleInfo(models.Model):
    """人物信息表"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
