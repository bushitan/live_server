#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *
# from cover.models import *


# 背景图
class Background(AppBase):
	user =  models.ForeignKey(User, verbose_name=u'所属用户',null=True,blank=True)
	url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
	# style = models.IntegerField(u'类别',default=FILE_IMAGE,choices=FILE_STYLE.items(),)
	local_path = models.ImageField(u'图标',upload_to='static/img/',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'背景'

	def __unicode__(self):
		return '%s' % (self.id)

# 舞台——系统提供内容
class Stage(AppBase):
	# teacher =  models.ForeignKey(User, verbose_name=u'老师',null=True,blank=True)
	background =  models.ForeignKey(Background, verbose_name=u'背景图片',null=True,blank=True)
	config =  models.TextField( verbose_name=u'配置',null=True,blank=True)
	# teacher_player =  models.CharField(max_length=100, verbose_name=u'教室播放地址',null=True,blank=True)
	# student_pusher =  models.CharField(max_length=100, verbose_name=u'学生推流地址',null=True,blank=True)
	# student_player =  models.CharField(max_length=100, verbose_name=u'学生播放地址',null=True,blank=True)
	# key =  models.CharField(max_length=32, verbose_name=u'秘钥',null=True,blank=True)
	# create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'舞台'
	def __unicode__(self):
		return '%s' % (self.id)