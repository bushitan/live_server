#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *

WEB_SITE =  {
	0:u"留学",
	1:u"移民",
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
class MGRTag(AppBase):
	web_site = models.IntegerField(u'所属网站',default=0,choices=WEB_SITE.items(),)
	father = models.ForeignKey( "self", verbose_name=u'父类栏目',null=True,blank=True)
	pid = models.IntegerField(u'pid',null=True,blank=True)
	class Meta:
		verbose_name_plural = verbose_name = u'栏目'
		ordering = ['-serial']

	def __unicode__(self):
		return '%s' % (self.name_admin)

#8 文章库
class MGRArticle(AppBase):
	tag = models.ForeignKey( MGRTag, verbose_name=u'所属栏目',null=True,blank=True)
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
