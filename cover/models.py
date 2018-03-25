#coding:utf-8
from django.db import models
from room.models import *
from lib.util import *
from lib.image_save import *
from lite.models import *
# Create your models here.

#文章标签
class Tag(AppBase):
    des = models.TextField( verbose_name=u'描述',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'标签'
        ordering = ['-serial']

    def __unicode__(self):
        return '%s' % (self.name_admin)

# 日程
class News(AppBase):
    article =  models.ForeignKey('Article',verbose_name=u'链接文章',null=True,blank=True) #所属会议
    tag =  models.ForeignKey('Tag',verbose_name=u'所属标签',null=True,blank=True) #所属会议
    cover_image = models.ForeignKey(FileLibrary, verbose_name=u'封面图片',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    summary = models.CharField(max_length=100, verbose_name=u'摘要',null=True,blank=True)
    des = models.CharField(max_length=100, verbose_name=u'详细描述',null=True,blank=True)
    footer = models.CharField(max_length=100, verbose_name=u'页脚',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'封面大图'
        ordering = ['-create_time']

    def __unicode__(self):
        return '%s' % (self.id)

#8 文章库
class Article(AppBase):

    click_rate = models.IntegerField(u'点击率',default=8965)
    style = models.IntegerField(u'文章类别',default=ARTICLE_STYLE_NORMAL,choices=ARTICLE_STYLE.items(),)
    #NO.1 直播模式
    room =  models.ForeignKey('room.Room', verbose_name=u'直播房间',related_name="rrr",null=True,blank=True)

    #文章内容
    title = models.CharField(max_length=100, verbose_name=u'标题',null=True,blank=True)
    subtitle = models.CharField(max_length=100,verbose_name=u'子标题',default='',null=True,blank=True)
    #摘要 发布时间
    summary = models.CharField(max_length=100,verbose_name=u'摘要',default='',null=True,blank=True)
    source = models.CharField(max_length=100,verbose_name=u'来源',default='',null=True,blank=True)
    #正文
    content = models.TextField(verbose_name=u'正文',null=True,blank=True)
    content_width = models.IntegerField(verbose_name=u'正文显示宽度',default=750,null=True,blank=True)


    #音频
    audio_src = models.CharField(max_length=1000,verbose_name=u'音频地址(Url)',null=True,blank=True)
    audio_poster = models.CharField(max_length=500,verbose_name=u'音频封面图(Url)',null=True,blank=True)
    audio_name = models.CharField(max_length=100,verbose_name=u'音频名称',null=True,blank=True)
    audio_author = models.CharField(max_length=100,verbose_name=u'音频作者',null=True,blank=True)

    #视频
    video_src = models.CharField(max_length=1000,verbose_name=u'视频地址(Url)',null=True,blank=True)

    #地址，IS_SHOW
    address = models.CharField(max_length=200, verbose_name=u'地址',default="",null=True,blank=True)
    work_date = models.CharField(max_length=200, verbose_name=u'工作时间',default="",null=True,blank=True)
    phone = models.CharField(max_length=40, verbose_name=u'电话',default="",null=True,blank=True)
    introduction = models.CharField(max_length=500, verbose_name=u'简介',default="",null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'文章'
        ordering = ['-issue_time', '-is_top']
        # ordering = ['rank', '-is_top', '-pub_time', '-create_time']

    def __unicode__(self):
            return self.title

