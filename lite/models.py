#coding:utf-8
from django.db import models
from lib.util import *
# Create your models here.
import django.utils.timezone as timezone

from lib.image_save import *
from django.db import models
from django.contrib.auth.models import AbstractUser

# class AdminUser(AbstractUser):
#     address = models.CharField(max_length=100)

from django.contrib.auth.models import User as  AdminUser
# class UserProfile(models.Model):
#     user = models.OneToOneField(AdminUser)
#     app =  models.ForeignKey( 'App', verbose_name=u'所属小程序',null=True,blank=True)


#企业信息
class App(models.Model):
    sys_user = models.OneToOneField(AdminUser,related_name=u"system_user",verbose_name=u'系统管理员',null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    app_id =  models.CharField(max_length=100, verbose_name=u'AppID',null=True,blank=True)
    secret_key = models.CharField(max_length=100, verbose_name=u'SecretKey',null=True,blank=True)
    im_num =  models.CharField(max_length=100, verbose_name=u'IM房间号',null=True,blank=True)
    pusher =  models.CharField(max_length=500, verbose_name=u'推流地址',null=True,blank=True)
    player =  models.CharField(max_length=500, verbose_name=u'播放地址',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'APP应用'

    def __unicode__(self):
        return '%s' % (self.name)


#企业信息
class AppBase(models.Model):
    app =  models.ForeignKey( App, verbose_name=u'所属小程序',default=1)
    name =  models.CharField(max_length=100, verbose_name=u'小程序显示名称',default="",null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'后台显示名称',default="",null=True,blank=True)
    is_top = models.IntegerField(u'是否指定',default=YES,choices=IS_TOP.items(),)
    is_show = models.IntegerField(u'是否显示',default=YES,choices=IS_SHOW.items(),)
    is_alive = models.IntegerField( verbose_name=u'是否有效',default=YES,choices=IS_ALIVE.items())
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    issue_time = models.DateTimeField(u'发布时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        abstract = True




#7 图片库
class FileLibrary(AppBase):
    # app =  models.ForeignKey( App, verbose_name=u'所属小程序',null=True,blank=True)
    # user =  models.ForeignKey('User', verbose_name=u'所属用户',null=True,blank=True)
    file_tag =  models.ForeignKey('FileTag', verbose_name=u'所属标签',null=True,blank=True)
    # name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    style = models.IntegerField(u'类别',default=FILE_IMAGE,choices=FILE_STYLE.items(),)
    local_path = models.ImageField(u'图标',upload_to='static/img/',default="",null=True,blank=True)
    # create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'图库'

    def __unicode__(self):
        return '%s' % (self.id)

#7 图片库
class FileTag(AppBase):
    # app =  models.ForeignKey( App, verbose_name=u'所属小程序',null=True,blank=True)
    # name = models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    # create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'图库标签'
    def __unicode__(self):
        return '%s' % (self.name_admin)



class User(AppBase):
    # models.ImageField()
    # app =  models.ForeignKey( App, verbose_name=u'所属小程序',null=True,blank=True)
    # logo = models.CharField(max_length=300, verbose_name=u'logo链接',default="",null=True,blank=True)
    # logo = models.ImageField(max_length=150, verbose_name=u'logo链接',null=True,blank=True)
    # name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    wx_id =  models.CharField(max_length=100, verbose_name=u'微信号',null=True,blank=True)

    user_name =  models.CharField(max_length=100, verbose_name=u'姓名',null=True,blank=True)
    #微信信息
    nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',null=True,blank=True)
    avatar_url =  models.CharField(max_length=500, verbose_name=u'头像',null=True,blank=True)
    gender =  models.CharField(max_length=100, verbose_name=u'性别',null=True,blank=True)
    province =  models.CharField(max_length=100, verbose_name=u'位置',null=True,blank=True)
    city =  models.CharField(max_length=100, verbose_name=u'国家',null=True,blank=True)
    country =  models.CharField(max_length=100, verbose_name=u'城市',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)

    is_teacher =  models.IntegerField(u'是否讲师',default=NO,choices=IS_TEACHER.items(),)


    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
    wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey过期时间',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
    expires = models.FloatField( verbose_name=u'Django的session过期时间',null=True,blank=True)
    uuid =  models.CharField(max_length=32, verbose_name=u'uuid标识',null=True,blank=True)
    # create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'用户'
        # app_label = string_with_title(u'api', u"23421接口")

    def __unicode__(self):
        return '%s' % (self.id)

#企业信息
class Company(AppBase):
    # app =  models.ForeignKey( App, verbose_name=u'所属小程序',null=True,blank=True)
    # name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'手机',null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'个人简介',default="",null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    latitude = models.FloatField(verbose_name=u'纬度',default=0)
    longitude = models.FloatField(verbose_name=u'精度',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'联系方式'

    def __unicode__(self):
        return '%s' % (self.name)
