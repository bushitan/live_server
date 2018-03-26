#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *


class BackgroundAdmin(AppAdmin):
	list_display = ("id","cover_pre","user",)
	temp_suit_form_tabs = (('content', u'背景图片'),)
	temp_fieldsets = (
		(u"封面", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["user","url","local_path",]
		}),
    )
	def cover_pre(self, obj):
		html = u"未添图片"
		if obj.url is not None:
			html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.url)
		return html
	cover_pre.short_description = u'背景预览'
	cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
	readonly_fields = ['cover_pre',] #图片一定要只读
	# raw_id_fields = ('user','room',)
admin.site.register(Background,BackgroundAdmin)

class StageAdmin(AppAdmin):
	list_display = ("id","cover_pre","config",)
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"封面", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["background","config",]
		}),
    )
	def cover_pre(self, obj):
		html = u"未添图片"
		if obj.background is not None:
			html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.background.url)
		return html
	cover_pre.short_description = u'背景预览'
	cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
	readonly_fields = ['cover_pre',] #图片一定要只读
	# raw_id_fields = ('user','room',)
admin.site.register(Stage,StageAdmin)
