#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *
# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = UserProfile
#     verbose_name = 'profile'
#
# class UserAdmin(admin.ModelAdmin):
#     inlines = (ProfileInline,)
#
# admin.site.register(User,UserAdmin)



# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile,UserProfileAdmin)

class LiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(App,LiteAdmin)

class UserAdmin(AppAdmin):
    list_display = ("id","avatar","user_name","nick_name","phone","is_teacher",)
    temp_suit_form_tabs = (('content', u'微信信息'),)
    def get_form(self, request, obj=None, *args, **kwargs):
        _fieldsets = (
                (u"个人资料", {
                    'classes': ('suit-tab', 'suit-tab-content',),
                    'fields': ['is_teacher','user_name']
                }),
                (u"微信资料", {
                    'classes': ('suit-tab', 'suit-tab-content',),
                    'fields': ['avatar','wx_id','nick_name','avatar_url','gender','province','city','country','phone',]
                }),
            )
        if request.user.is_superuser is True:
            #超级用户，可以看详细信息
            self.temp_fieldsets = _fieldsets + (
                (u"验证信息", {
                    'classes': ('suit-tab', 'suit-tab-content',),
                    'fields': ['wx_open_id','wx_session_key','wx_expires_in','session','expires','uuid',]
                }),
            )
        else:
            self.temp_fieldsets = _fieldsets
        return super(UserAdmin, self).get_form(request,obj, **kwargs)

    def avatar(self, obj):
        html = u"未添图片"
        if obj.avatar_url != "":
            html = u'<img src="%s" style="width:48px;height:48px" />' %(obj.avatar_url)
        return html
    avatar.short_description = u'头像'
    avatar.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['avatar',] #图片一定要只读
admin.site.register(User,UserAdmin)

# 文件存储
class FileLibraryAdmin(AppAdmin):
    list_display = ("cover_pre","file_tag","style","local_path",)
    temp_suit_form_tabs = (('content', u'图片编辑'),)
    temp_fieldsets = (
        (u"上传预览", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['cover_pre','url','style','local_path',]
        }),

        (u"分类", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['file_tag']
        }),
    )
    def cover_pre(self, obj):
        html = u"未添图片"
        if obj.url != "":
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.url)
        return html
    cover_pre.short_description = u'图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',] #图片一定要只读
    raw_id_fields = ('file_tag',)
admin.site.register(FileLibrary,FileLibraryAdmin)
# 文件标签
class FileTagAdmin(AppAdmin):
    pass
admin.site.register(FileTag,FileTagAdmin)


class CompanyAdmin(AppAdmin):
    temp_suit_form_tabs = (('content', u'公司内容'),)
    temp_fieldsets = (
        (u"上传预览", {
            'classes': ('suit-tab', 'suit-tab-content',),
            'fields': ['introduction','phone','address','latitude','longitude',]
        }),
    )
admin.site.register(Company,CompanyAdmin)