#coding:utf-8
from django.db import models
from lib.util import *
# Create your models here.
import django.utils.timezone as timezone

class User(models.Model):
    # models.ImageField()
    logo = models.CharField(max_length=300, verbose_name=u'logo链接',default="",null=True,blank=True)
    # logo = models.ImageField(max_length=150, verbose_name=u'logo链接',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    nick_name =  models.CharField(max_length=100, verbose_name=u'微信昵称',null=True,blank=True)
    wx_id =  models.CharField(max_length=100, verbose_name=u'微信号',null=True,blank=True)

    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
    wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey过期时间',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
    expires = models.FloatField( verbose_name=u'Django的session过期时间',null=True,blank=True)
    uuid =  models.CharField(max_length=32, verbose_name=u'uuid标识',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)

    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'用户_基本信息'
        # app_label = string_with_title(u'api', u"23421接口")

    def __unicode__(self):
        return '%s' % (self.id)

#企业信息
class Company(models.Model):
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    latitude = models.FloatField(verbose_name=u'精度',default=0)
    longitude = models.FloatField(verbose_name=u'维度',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'机构展示信息'

    def __unicode__(self):
        return '%s' % (self.name)
