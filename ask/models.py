#  -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth import models as auth_model
from utils import base62
__author__ = 'copyliu'

class BoxModel(models.Model):
    user= models.OneToOneField(auth_model.User,unique=True)

    # TODO 扩充字段
    @property
    def sid(self):
        return base62.dehydrate(self.pk)
class Asks (models.Model):
    box=models.ForeignKey('BoxModel')
    # title=models.TextField()
    body=models.TextField()
    add_date=models.DateTimeField(auto_now_add=True)
    deleted=models.BooleanField(default=False)
    del_date=models.DateTimeField(null=True)
    spam_flag=models.BooleanField(default=False)
    read_flag=models.BooleanField(default=False)
    read_date=models.DateTimeField(null=True)



