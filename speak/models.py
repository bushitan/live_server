#coding:utf-8
from django.db import models
from room.models import *
from lib.util import *
from lib.image_save import *
from lite.models import *
# Create your models here.


class SpeakTheme(AppBase):
	title =  models.CharField(max_length=100, verbose_name=u'题目',default="",null=True,blank=True)
	content =  models.TextField(verbose_name=u'内容',default="",null=True,blank=True)
	voice = models.ForeignKey(FileLibrary, verbose_name=u'老师示范录音', related_name='speak_teacher_voice',null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'拼读题目'
		ordering = ['-serial']
	def __unicode__(self):
		return '%s' % (self.id)
#文章标签
class SpeakUser(AppBase):
	theme = models.ForeignKey(SpeakTheme ,verbose_name=u'所属题目',null=True,blank=True)
	user = models.ForeignKey(User,related_name=u"speak_user",verbose_name=u'说英语用户',null=True,blank=True)
	voice = models.ForeignKey(FileLibrary, verbose_name=u'录音', related_name='speak_user_voice',null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'用户提交作业'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)

#会员积分
class SpeakBonus(AppBase):
	user_self = models.ForeignKey(User,related_name=u"bonus_self",verbose_name=u'自己',null=True,blank=True)
	user_other = models.ForeignKey(User,related_name=u"bonus_other",verbose_name=u'对方',null=True,blank=True)
	theme = models.ForeignKey(SpeakTheme ,verbose_name=u'所属题目',null=True,blank=True)
	action = models.IntegerField(u'操作',choices=SPEAK_ACTION.items(),null=True,blank=True)
	score = models.IntegerField(u'分数',null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'用户积分'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.user_self)