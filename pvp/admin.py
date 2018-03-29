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



class StageFileAdmin(AppAdmin):
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["url",'style','local_path',]
		}),
    )
admin.site.register(StageFile,StageFileAdmin)

class StageTagAdmin(AppAdmin):
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["description",]
		}),
    )
admin.site.register(StageTag,StageTagAdmin)

class StageAdmin(AppAdmin):
	list_display = ("id","cover_pre","name","name_admin",'serial',)
	temp_suit_form_tabs = (('content', u'舞台配置'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["tag",]
		}),
		(u"舞台参数", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["background_image","cover_image","audio_image","orientation","width","height",]
		}),
		(u"录制参数", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["pusher_image","pusher_x","pusher_y","pusher_width","pusher_height",]
		}),
		(u"播放参数", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["player_image","player_x","player_y","player_width","player_height",]
		}),
    )
	def cover_pre(self, obj):
		html = u"未添图片"
		if obj.cover_image is not None:
			html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
		return html
	cover_pre.short_description = u'背景预览'
	cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
	readonly_fields = ['cover_pre',] #图片一定要只读
	# raw_id_fields = ('user','room',)
admin.site.register(Stage,StageAdmin)



class PVPMemberAdmin(AppAdmin):
	list_display = ("id","user","start_time","end_time",'is_alive',)
	temp_suit_form_tabs = (('content', u'会员'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["user",'start_time','end_time',]
		}),
    )
admin.site.register(PVPMember,PVPMemberAdmin)





















