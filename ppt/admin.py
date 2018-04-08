#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *




class StageFileAdmin(AppAdmin):
	list_filter = ('style',)
	temp_list_display = ('style',)
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["url",'style','local_path',]
		}),
    )
admin.site.register(PPTFile,StageFileAdmin)

class StageTagAdmin(AppAdmin):
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["description",]
		}),
    )
admin.site.register(PPTTag,StageTagAdmin)















