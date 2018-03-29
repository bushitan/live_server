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



#7 图片库
class StageFile(AppBase):
	# file_tag =  models.ForeignKey('FileTag', verbose_name=u'所属标签',null=True,blank=True)
	url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
	style = models.IntegerField(u'类别',default=FILE_IMAGE,choices=FILE_STYLE.items(),)
	local_path = models.ImageField(u'图标',upload_to='static/img/',default="",null=True,blank=True)
	# create_time = models.DateTimeField(u'创建时间', default = timezone.now)
	class Meta:
		verbose_name_plural = verbose_name = u'图库'

	def __unicode__(self):
		return '%s' % (self.id)


#文章标签
class StageTag(AppBase):
	description = models.CharField(max_length=100,  verbose_name=u'简介',null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'标签'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)



VERTICAL = 0
HORIZONTAL = 1
STAGE_ORIENTATION = {
    VERTICAL:u"水平",
    HORIZONTAL:u"竖直",
}
# 舞台——系统提供内容
class Stage(AppBase):
	# teacher =  models.ForeignKey(User, verbose_name=u'老师',null=True,blank=True)
	tag =  models.ForeignKey(StageTag,verbose_name=u'所属标签',null=True,blank=True) #所属会议
	background_image =  models.ForeignKey(StageFile, verbose_name=u'背景图片',related_name="background_image",null=True,blank=True)
	cover_image =  models.ForeignKey(StageFile, verbose_name=u'封面图片',related_name="cover_image",null=True,blank=True)
	audio_image =  models.ForeignKey(StageFile, verbose_name=u'背景音乐',related_name="audio_image",null=True,blank=True)
	orientation = models.IntegerField(u'方向',default=VERTICAL,choices=STAGE_ORIENTATION.items(),)
	width = models.CharField(max_length=20, verbose_name=u'宽度',null=True,blank=True)
	height = models.CharField(max_length=20, verbose_name=u'高度',null=True,blank=True)

	pusher_image = models.ForeignKey(StageFile, verbose_name=u'录制遮盖图片',related_name="pusher_image",null=True,blank=True)
	pusher_x = models.CharField(max_length=20, verbose_name=u'录制x',null=True,blank=True)
	pusher_y = models.CharField(max_length=20, verbose_name=u'录制y',null=True,blank=True)
	pusher_width = models.CharField(max_length=20, verbose_name=u'录制宽度',null=True,blank=True)
	pusher_height = models.CharField(max_length=20, verbose_name=u'录制高度',null=True,blank=True)

	player_image = models.ForeignKey(StageFile, verbose_name=u'播放遮盖图片',related_name="player_image",null=True,blank=True)
	player_x = models.CharField(max_length=20, verbose_name=u'播放x',null=True,blank=True)
	player_y = models.CharField(max_length=20, verbose_name=u'播放y',null=True,blank=True)
	player_width = models.CharField(max_length=20, verbose_name=u'播放宽度',null=True,blank=True)
	player_height = models.CharField(max_length=20, verbose_name=u'播放高度',null=True,blank=True)


	# background =  models.ForeignKey(Background, verbose_name=u'背景图片',null=True,blank=True)
	# config =  models.TextField( verbose_name=u'配置',null=True,blank=True)

	# teacher_player =  models.CharField(max_length=100, verbose_name=u'教室播放地址',null=True,blank=True)
	# student_pusher =  models.CharField(max_length=100, verbose_name=u'学生推流地址',null=True,blank=True)
	# student_player =  models.CharField(max_length=100, verbose_name=u'学生播放地址',null=True,blank=True)
	# key =  models.CharField(max_length=32, verbose_name=u'秘钥',null=True,blank=True)
	# create_time = models.DateTimeField(u'创建时间',default = timezone.now,null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'舞台'
	def __unicode__(self):
		return '%s' % (self.id)


class PVPMember(AppBase):
	user = models.ForeignKey(User, verbose_name=u'用户',null=True,blank=True)
	# is_alive = models.IntegerField( verbose_name=u'是否有效',default=YES,choices=IS_ALIVE.items())
	start_time = models.DateTimeField(u'开始时间', default = timezone.now)
	end_time = models.DateTimeField(u'结束时间', default = timezone.now)
	# 点击链接的文章
	class Meta:
		verbose_name_plural = verbose_name = u'会员'
		ordering = ['-create_time']
	def __unicode__(self):
		return '%s' % (self.id)



















