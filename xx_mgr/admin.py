#coding:utf-8
from django.contrib import admin
from models import *
from live_server.settings import *
from lib.admin_config import *

class MGRTagAdmin(AppAdmin):

	# fieldsets = ('web_site',"father",)
	list_display = ("id","is_show",'web_site',"father","pid","name","name_admin","serial",)
	suit_form_tabs = (('content', u'栏目编辑'),)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['web_site',"father","pid","name","name_admin","serial",]
		}),
    )
	list_editable = ('web_site',"father","name","name_admin","serial","pid",)
	list_filter = ('web_site',"father",)

admin.site.register(MGRTag,MGRTagAdmin)

class MGRArticleAdmin(AppAdmin):

	list_display = ("id","is_show",'tag',"title","subtitle")
	# list_display = ("id","style","title","is_top","is_show","is_alive","serial","issue_time",)
	suit_form_tabs = (('content', u'文章内容编辑'),)
	# raw_id_fields = ('room',)
	fieldsets = (
		(u"标题", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['tag','title','subtitle']
		}),
		(u"留学模块填写", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["lx_item","lx_know"]
		}),
		(u"属性", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["click_rate","issue_time"]
		}),
		(u"正文", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['summary',"source",'content',]
		}),
    )
	# list_editable = ('tag',)
	list_filter = ('tag',)
	raw_id_fields = ('tag',)
	class Media:
		js = ( STATIC_URL + 'tinymce/tinymce.min.js',
			   STATIC_URL + 'tinymce/textareas.js')
admin.site.register(MGRArticle,MGRArticleAdmin)


