#coding:utf-8
from lite.models import *
from cover.models import *
from django.contrib import admin

def AppGetID(request):
    admin_user_id = request.user.id
    _app = App.objects.get(sys_user_id = admin_user_id)
    return _app.id

def AppFilterQuerySet(self,request,admin):
    qs = super(admin, self).get_queryset(request)
    if request.user.is_superuser:
        return qs
    else:
        # APP已经绑定管理用户
        if App.objects.filter(sys_user_id = request.user.id).exists() is True:
            _app = App.objects.get(sys_user_id = request.user.id)
            return qs.filter(app_id = _app.id)
        else:
            print u'APP 未绑定用户'


    #定义基础的tab，过后
base_list_display = ("id","app","name","name_admin","is_top","is_show","is_alive","serial","issue_time","create_time",)
base_suit_form_tabs = (('param', u'基础属性'),)
base_fieldsets  = (
    (u"名称", {
        'classes': ('suit-tab', 'suit-tab-param',),
        'fields': ['app','name','name_admin']
    }),
    (u"显示", {
        'classes': ('suit-tab', 'suit-tab-param',),
        'fields': ['is_top','is_show','is_alive','serial',]
    }),
    (u"时间", {
        'classes': ('suit-tab', 'suit-tab-param',),
        'fields': ['issue_time','create_time']
    }),
)

class AppAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return AppFilterQuerySet(self,request,AppAdmin)
    def get_changeform_initial_data(self, request):
        if request.user.is_superuser is False:
            return {'app': AppGetID(request)}
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser is False:
            if db_field.name == "app":
                kwargs["queryset"] =  App.objects.filter(id = AppGetID(request))
        return super(AppAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    fieldsets = base_fieldsets
    suit_form_tabs = base_suit_form_tabs
    temp_list_display = ()
    temp_fieldsets = ()
    temp_suit_form_tabs = ()
    def get_list_display(self, request):
        #有原始的列表
        if  self.list_display == ('__str__',):
            return self.temp_list_display  + base_list_display
        return self.list_display

    # 前两个点击进入
    def get_list_display_links(self, request, list_display):
        if self.list_display_links or not list_display:
            return self.list_display_links
        else:
            return list(list_display)[:2]

    def get_form(self, request, obj=None,*args, **kwargs):
        if self.temp_fieldsets != ():
            self.fieldsets = self.temp_fieldsets  + base_fieldsets
        # print self.fieldsets

        if self.temp_suit_form_tabs != ():
            self.suit_form_tabs = self.temp_suit_form_tabs  + base_suit_form_tabs
        # print self.suit_form_tabs
        return super(AppAdmin, self).get_form(request, obj, **kwargs)



#文章的form样式
def ArticleDetail(style):
    def Text():
        _tuple = (
            (u"展示", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['style',]
            }),
            (u"标题", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['title','subtitle','summary','source',]
            }),
            (u"正文", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['content','content_width',]
            }),
        )
        return _tuple

    # 纯文字
    def Audio():
        _tuple = (
            (u"展示", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['is_show','style',]
            }),
            (u"标题", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['title','subtitle','summary','source',]
            }),
        )
        return _tuple

    def Video():
        _tuple = (
            (u"展示", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['style',]
            }),
            (u"视频", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['video_src',]
            }),
            (u"标题", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['title','subtitle','summary','source',]
            }),
            (u"正文", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['content','content_width',]
            }),
        )
        return _tuple

    def Live():
        _tuple = (
            (u"模板选择", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['style',]
            }),
            (u"录播房间", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['room',]
            }),
        )
        return _tuple

    def Normal():
        _tuple = (
            (u"模板选择", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['style',]
            }),
            (u"标题", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['room',]
            }),
            (u"正文", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['content_width','content',]
            }),
            (u"音频", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['audio_src','audio_poster','audio_name','audio_author',]
            }),
            (u"视频", {
                'classes': ('suit-tab', 'suit-tab-base',),
                'fields': ['video_src']
            }),
        )
        return _tuple



    if style == ARTICLE_STYLE_TEXT:
        return Text()
    if style == ARTICLE_STYLE_AUDIO:
        return Audio()
    if style == ARTICLE_STYLE_VIDEO:
        return Video()
    if style == ARTICLE_STYLE_LIVE:
        return Live()

    return Normal()


#
# def SuitFormTabs(suit_form_tabs):
#     return suit_form_tabs + (('param', u'基础属性'),)
# def SuitFieldsets(fieldsets):
#     return fieldsets + (
#         (u"名称", {
#             'classes': ('suit-tab', 'suit-tab-param',),
#             'fields': ['app','name','name_admin']
#         }),
#         (u"显示", {
#             'classes': ('suit-tab', 'suit-tab-param',),
#             'fields': ['is_top','is_show','is_alive','serial',]
#         }),
#         (u"时间", {
#             'classes': ('suit-tab', 'suit-tab-param',),
#             'fields': ['issue_time','create_time']
#         }),
#     )
