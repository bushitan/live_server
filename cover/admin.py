#coding:utf-8
from django.contrib import admin
from models import *
from live_server.settings import *
from lib.admin_config import *
# Register your models here.

class TagAdmin(AppAdmin):
    pass
admin.site.register(Tag,TagAdmin)

class ArticleAdmin(AppAdmin):
    list_display = ("id","style","room","title","is_top","is_show","is_alive","serial","issue_time",)
    temp_suit_form_tabs = (('base', u'内容编辑'),)
    temp_fieldsets = (
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
    # def get_form(self, request, obj=None, *args, **kwargs):
    #     print 38748923789,obj
    #     if obj is not None:
    #         print obj.style
    #         self.temp_fieldsets = ArticleDetail(obj.style)  #当前文章的样式
    #         print self.temp_fieldsets
    #     else:
    #         self.temp_fieldsets = ArticleDetail( ARTICLE_STYLE_NORMAL)  #默认样式
    #     return super(ArticleAdmin, self).get_form(request,obj, **kwargs)

    raw_id_fields = ('room',)
    class Media:
        js = ( STATIC_URL + 'tinymce/tinymce.min.js',
               STATIC_URL + 'tinymce/textareas.js')
admin.site.register(Article,ArticleAdmin)


class NewsAdmin(AppAdmin):
    list_display = ("id","cover_pre","article","tag","title","summary","des",)
    temp_fieldsets = (
        (u"展示信息", {
            'classes': ('suit-tab', 'suit-tab-news',),
            'fields': ['cover_pre','cover_image','title','summary','des','footer',]
        }),
        (u"指向内容", {
            'classes': ('suit-tab', 'suit-tab-news',),
            'fields': ['article',]
        }),
        (u"所属标签", {
            'classes': ('suit-tab', 'suit-tab-news',),
            'fields': ['tag',]
        }),
    )
    temp_suit_form_tabs = (('news', u'封面编辑'),)
    def cover_pre(self, obj):
        html = u"未添图片"
        if obj.cover_image != "":
            html = u'<img src="%s" style="width:72px;height:48px" />' %(obj.cover_image.url)
        return html
    cover_pre.short_description = u'封面图片预览'
    cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
    readonly_fields = ['cover_pre',]
    raw_id_fields = ('cover_image','article','tag',)

    # 外键过滤
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if request.user.is_superuser is False:
    #         if db_field.name == "article":
    #             kwargs["queryset"] =  Article.objects.filter(app_id = AppGetID(request))
    #         if db_field.name == "tag":
    #             kwargs["queryset"] =  Tag.objects.filter(app_id = AppGetID(request))
    #     return super(AppAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(News,NewsAdmin)

    # def get_form(self, request, obj=None, *args, **kwargs):
    #     self._fieldsets = ArticleDetail(obj.style)
    #     self._suit_form_tabs = (('base', u'内容编辑'),)
    #     return super(ArticleAdmin, self).get_form(request,fieldsets, suit_form_tabs,obj, **kwargs)

    # def get_form(self, request, obj=None, *args, **kwargs):
    #     if obj is not None:
    #         self.fieldsets =ArticleDetail(obj.style)  + super(ArticleAdmin, self).fieldsets
    #         self.suit_form_tabs = (('base', u'内容编辑'),) + super(ArticleAdmin, self).suit_form_tabs
    #     return super(ArticleAdmin, self).get_form(request, obj, **kwargs)






    # self._fieldsets  =
    # fieldsets = (
    #     (u"名称", {
    #         'classes': ('suit-tab', 'suit-tab-base',),
    #         'fields': ['app','name','name_admin']
    #     }),
    # )
    # suit_form_tabs = (('base', u'哈哈'),)
    # def get_form(self, request, obj=None, *args, **kwargs):
    #     fieldsets = ()
    #     suit_form_tabs = ()
    #     return super(TagAdmin, self).get_form(request,fieldsets, suit_form_tabs,obj, **kwargs)
#     fieldsets  = (
#     (u"名称", {
#         'classes': ('suit-tab', 'suit-tab-param',),
#         'fields': ['app','name','name_admin']
#     }),
#     (u"显示", {
#         'classes': ('suit-tab', 'suit-tab-param',),
#         'fields': ['is_top','is_show','is_alive','serial',]
#     }),
#     (u"时间", {
#         'classes': ('suit-tab', 'suit-tab-param',),
#         'fields': ['issue_time','create_time']
#     }),
# )
    # def get_form(self, request, obj=None, *args, **kwargs):
    #     fieldsets  =  (u"测试", {
    #         'classes': ('suit-tab', 'suit-tab-base',),
    #         'fields': ['name',]
    #     })
    #     suit_form_tabs = (('base', u'内容编辑'),),
    #     return super(TagAdmin, self).get_form(request,fieldsets, suit_form_tabs,obj, **kwargs)




# class TagAdmin(admin.ModelAdmin):
#     # pass
#     def get_queryset(self, request):
#         return AppFilterQuerySet(self,request,TagAdmin)
#     def get_changeform_initial_data(self, request):
#         return {'app': AppGetID(request)}
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if request.user.is_superuser is False:
#             if db_field.name == "app":
#                 kwargs["queryset"] =  App.objects.filter(id = AppGetID(request))
#         return super(TagAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


        # qs = super(TagAdmin, self).get_queryset(request)
        # print 23984792
        # print request.user.id
        # _app = App.objects.get(sys_user_id = request.user.id)
        # return qs.filter(app_id = _app.id)



        # if request.user.is_superuser:
        #     return qs
    # return qs.filter(username=request.user.username,boss_verified=True)
    #  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #         if db_field.name == "tag":
    #             kwargs["queryset"] = Tag.objects.filter(Q(is_index = YES )| Q(is_ad =YES) | Q(is_swiper = YES) | Q(is_meet = YES) )
    #         return super(NewsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
