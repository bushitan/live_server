#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *

WEB_SITE =  {
	0:u"留学",
	1:u"移民",
	2:u"公共",
}
IS_NAVIGATION = {
	YES:u"导航",
	NO:u"隐藏",
}
# LX_NAV = {
# 	0:u"中小学",
# 	1:u"本科",
# 	2:u"硕士",
# 	3:u"我想了解",
# }
LX_ITEM = {
	0:u"专业解析",
	1:u"留学、移民方案",
	2:u"院校列表",
	3:u"申请时间规划表",
	4:u"申请攻略",
}
LX_KNOW = {
	0:u"留学新闻",
	1:u"院校资讯",
	2:u"专业推介",
	3:u"签证指南",
	4:u"院校排名",
	5:u"行前准备",
	6:u"留学规划",
	7:u"留学百问",
	8:u"海外奖学金",
	9:u"留学报告",
	10:u"备考资讯",
}

#7 图片库
class MGRKeyWord(AppBase):
	key_word =  models.CharField(max_length=100, verbose_name=u'关键字名称',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'关键字'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)


#7 图片库
class MGRTag(AppBase):
	web_site = models.IntegerField(u'所属网站',default=0,choices=WEB_SITE.items(),)
	father = models.ForeignKey( "self", verbose_name=u'父类栏目',null=True,blank=True)
	pid = models.IntegerField(u'pid',null=True,blank=True)

	logo = models.ForeignKey( "MGRImage", verbose_name=u'手机图标',null=True,blank=True)
	show_mobile = models.IntegerField(u'是否移动端显示',default=YES,choices=IS_SHOW.items(),)
	name_mobile = models.CharField(max_length=100, verbose_name=u'手机显示名称',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'栏目'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)

#8 文章库
class MGRArticle(AppBase):
	tag = models.ForeignKey( MGRTag, verbose_name=u'所属栏目',null=True,blank=True)
	cover = models.ForeignKey( "MGRImage", verbose_name=u'封面',null=True,blank=True)
	lx_item = models.IntegerField(u'子栏目',choices=LX_ITEM.items(),null=True,blank=True)
	lx_know = models.IntegerField(u'我想了解',choices=LX_KNOW.items(),null=True,blank=True)

	click_rate = models.IntegerField(u'点击率',default=8965)
	style = models.IntegerField(u'文章类别',default=ARTICLE_STYLE_NORMAL,choices=ARTICLE_STYLE.items(),)
	#NO.1 直播模式
	#文章内容
	title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
	subtitle = models.CharField(max_length=100,verbose_name=u'子标题',default='',null=True,blank=True)
	#摘要 发布时间
	summary = models.CharField(max_length=100,verbose_name=u'摘要',default='',null=True,blank=True)
	source = models.CharField(max_length=100,verbose_name=u'来源',default='',null=True,blank=True)
	#正文
	content = models.TextField(verbose_name=u'正文',null=True,blank=True)
	content_width = models.IntegerField(verbose_name=u'正文显示宽度',default=750,null=True,blank=True)

	class Meta:
		verbose_name_plural = verbose_name = u'文章'
		ordering = ['-issue_time']
		# ordering = ['rank', '-is_top', '-pub_time', '-create_time']

	def __unicode__(self):
			return self.title


IMAGE_STYLE = {
	0:u"上传",
	1:u"基础",
}

#7 图片库
class MGRImage(AppBase):

	style = models.IntegerField(u'图片类型',choices=IMAGE_STYLE.items(),default=0)
	url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
	local_path = models.ImageField(u'图标',upload_to='static/img/',default="",null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'图库'
	def __unicode__(self):
		return '%s' % (self.id)

	def save(self):
		#ID 为空，新增图片
		if self.local_path == "":
			super(MGRImage, self).save() #先保存一遍
			return

		if self.id is None:
			print "id 222"
			super(MGRImage, self).save() #先保存一遍
			print "id23255"
			QNUploadImage(self)


		#未保存前，获取原来的地址
		m = MGRImage.objects.get(id = self.id)
		_old_path = m.local_path.path if m.local_path != "" else ""
		super(MGRImage, self).save()

		#保存后，获取新地址
		_new_path = self.local_path.path if self.local_path !="" else ""
		print "3:",_new_path

		#地址没变化，直接保存
		if  _old_path == _new_path:
			return
		else:
			QNUploadImage(self)

#更新图片
def QNUploadImage(self):
	#获取本地地址
	_local_path = self.local_path.path
	_now = datetime.datetime.now()
	_name = "xx_mgr_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
	_style = _local_path.split(".")[-1] # 拼接类别
	_file_name = _name + "." + _style # 拼接图片名字
	self.url =  "http://img.12xiong.top/" + _file_name #存储的链接
	self.name = _file_name
	# #上传七牛
	_qiniu = QiNiu()
	print self.local_path.url
	print self.local_path.name
	_qiniu.put( "" , _file_name , _local_path )
	super(MGRImage, self).save()
