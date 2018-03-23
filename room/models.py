#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *
from cover.models import *
import django.utils.timezone as timezone
# Create your models here.

#房间
class Room(models.Model):
    app =  models.ForeignKey(App, verbose_name=u'所属小程序',null=True,blank=True)
    im_num =  models.CharField(max_length=100, verbose_name=u'IM房间号',null=True,blank=True)
    pusher =  models.CharField(max_length=500, verbose_name=u'推流地址',null=True,blank=True)
    player =  models.CharField(max_length=500, verbose_name=u'播放地址',null=True,blank=True)
    status = models.IntegerField(u'状态',default=ROOM_STATUS_PREPARE,choices=ROOM_STATUS.items(),)
    style = models.IntegerField(u'房间类型',default=ROOM_PREPARE,choices=ROOM_STYLE.items(),)
    # father =  models.ForeignKey('Tag',verbose_name=u'父目录',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'名称',null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'admin后台名称',null=True,blank=True)
    cover = models.ForeignKey(FileLibrary, verbose_name=u'主题封面', related_name='room_cover',null=True,blank=True)
    title =  models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    description =  models.CharField(max_length=100, verbose_name=u'描述',null=True,blank=True)
    content =  models.ForeignKey(FileLibrary, verbose_name=u'内容图片', related_name='room_content',null=True,blank=True)
    serial =  models.IntegerField(verbose_name=u'排序',default=0)
    is_show = models.IntegerField(u'是否显示',default=YES,choices=IS_SHOW.items(),)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
    # des = models.TextField( verbose_name=u'描述',null=True,blank=True)
    # is_show = models.IntegerField(u'是否在首页显示标签',default=YES,choices=IS_SHOW.items(),)
    # serial =  models.IntegerField(verbose_name=u'排序',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'聊天室'
        ordering = ['-serial']

    def __unicode__(self):
        return '%s' % (self.id)


class Classroom(models.Model):
    app =  models.ForeignKey(App, verbose_name=u'所属小程序',null=True,blank=True)
    teacher =  models.ForeignKey(User, verbose_name=u'老师',null=True,blank=True)
    teacher_pusher =  models.CharField(max_length=100, verbose_name=u'教室推流地址',null=True,blank=True)
    teacher_player =  models.CharField(max_length=100, verbose_name=u'教室播放地址',null=True,blank=True)
    student_pusher =  models.CharField(max_length=100, verbose_name=u'学生推流地址',null=True,blank=True)
    student_player =  models.CharField(max_length=100, verbose_name=u'学生播放地址',null=True,blank=True)
    key =  models.CharField(max_length=32, verbose_name=u'秘钥',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'1v1教室'
    def __unicode__(self):
        return '%s' % (self.id)


#信息
class Message(models.Model):
    room =  models.ForeignKey(Room, verbose_name=u'所属聊天室',null=True,blank=True)
    user =  models.ForeignKey(User, verbose_name=u'用户',null=True,blank=True)
    style =  models.IntegerField(u'类型',default=MESSAGE_TEXT,choices=MESSAGE_STYLE.items(),)
    is_teacher =  models.IntegerField(u'是否讲师发言',default=YES,choices=IS_TEACHER.items(),)
    text =  models.CharField(max_length=400, verbose_name=u'文字',null=True,blank=True)
    image = models.CharField(max_length=500, verbose_name=u'图片',default="",null=True,blank=True)
    audio = models.CharField(max_length=500, verbose_name=u'语音',default="",null=True,blank=True)

    # image =  models.ForeignKey(FileLibrary, verbose_name=u'图片',related_name='message_image',null=True,blank=True)
    # audio =  models.ForeignKey(FileLibrary, verbose_name=u'语音',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'官方信息'
        # ordering = ['-serial']
    def __unicode__(self):
        return '%s' % (self.id)

#推流用户
class PusherUser(models.Model):
    # room =  models.ForeignKey(Room, verbose_name=u'所属聊天室',null=True,blank=True)
    app =  models.ForeignKey(App, verbose_name=u'所属小程序',null=True,blank=True)
    user =  models.ForeignKey(User, verbose_name=u'用户',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'推流用户'
        # ordering = ['-serial']
    def __unicode__(self):
        return '%s' % (self.id)









