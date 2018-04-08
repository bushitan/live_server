#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *
# from cover.models import *

#7 图片库
class PPTFile(AppBase):
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
class PPTTag(AppBase):
	description = models.CharField(max_length=100,  verbose_name=u'简介',null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'标签'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)


















