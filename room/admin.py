#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *

class RoomAdmin(AppAdmin):
    list_display = ("cover_pre","title","description","content",)
    temp_suit_form_tabs = (('content', u'图片编辑'),)
    temp_fieldsets = (
        (u"封面", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['cover_pre','cover','title','description','content_pre','content',]
        }),
        (u"状态", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['status','style',]
        }),
    )
    raw_id_fields = ('cover','content',)

    def cover_pre(self, obj):
        html = u"未添图片"
        if obj.cover is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover.url)
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    def content_pre(self, obj):
        html = u"未添图片"
        if obj.content is not None:
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.content.url)
        return html
    content_pre.short_description = u'内容图片预览'
    content_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre','content_pre'] #图片一定要只读
admin.site.register(Room,RoomAdmin)


class MessageAdmin(AppAdmin):
    list_display = ("room","user","is_teacher","style","text","image","audio",)
    temp_suit_form_tabs = (('content', u'信息'),)
    temp_fieldsets = (
        (u"封面", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ["room","user","is_teacher","style","text","image","audio",]
        }),
    )
    raw_id_fields = ('user','room',)
admin.site.register(Message,MessageAdmin)


# class PusherUserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(PusherUser,PusherUserAdmin)



# class ClassroomAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Classroom,ClassroomAdmin)
