#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *




class PPTFileAdmin(AppAdmin):
	list_filter = ('style',)
	list_display = ('id','tag','style','upload_user',)
	temp_suit_form_tabs = (('content', u'文件信息'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['tag',"url",'style','local_path','upload_user',]
		}),
    )
admin.site.register(PPTFile,PPTFileAdmin)

class PPTTagAdmin(AppAdmin):
	list_display = ('id','name','team','user','app',)
	suit_form_tabs = (('content', u'标签信息'),)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['team','user',"name",'app',]
		}),
    )
	list_editable = ('app',)
admin.site.register(PPTTag,PPTTagAdmin)



class PPTTeamAdmin(AppAdmin):
	temp_list_display = ('id','create_user',)
	temp_suit_form_tabs = (('content', u'团队信息'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ["create_user",]
		}),
    )
admin.site.register(PPTTeam,PPTTeamAdmin)

class PPTTeamUserAdmin(AppAdmin):
	temp_list_display = ('id','team','member_user',)
	temp_suit_form_tabs = (('content', u'团队信息'),)
	temp_fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['team','member_user',]
		}),
    )
admin.site.register(PPTTeamUser,PPTTeamUserAdmin)




class PPTRosterTagAdmin(AppAdmin):
	list_display = ('id','team','name',)
	suit_form_tabs = (('content', u'部门信息'),)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['team','name',]
		}),
    )
admin.site.register(PPTRosterTag,PPTRosterTagAdmin)

class PPTRosterAdmin(AppAdmin):
	list_display = ('id','roster_tag','name','phone',)
	suit_form_tabs = (('content', u'人员信息'),)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['roster_tag','name','phone',]
		}),
    )
admin.site.register(PPTRoster,PPTRosterAdmin)










