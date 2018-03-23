#coding:utf-8
from django.contrib import admin
from models import *
from live_server.settings import *
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    # pass
    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        print 23984792
        print request.user.id
        _app = App.objects.get(sys_user_id = request.user.id)
        return qs.filter(app_id = _app.id)
        # if request.user.is_superuser:
        #     return qs
    # return qs.filter(username=request.user.username,boss_verified=True)
    #  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #         if db_field.name == "tag":
    #             kwargs["queryset"] = Tag.objects.filter(Q(is_index = YES )| Q(is_ad =YES) | Q(is_swiper = YES) | Q(is_meet = YES) )
    #         return super(NewsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Tag,TagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ( STATIC_URL + 'tinymce/tinymce.min.js',
               STATIC_URL + 'tinymce/textareas.js')
admin.site.register(Article,ArticleAdmin)

class NewsAdmin(admin.ModelAdmin):
    # pass
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser is False:
            if db_field.name == "tag":
                _app = App.objects.get(sys_user_id = request.user.id)
                kwargs["queryset"] =  Tag.objects.filter(app_id = _app.id)
        return super(NewsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


        # qs = super(NewsAdmin, self).get_queryset(request)
        # print 23984792
        # print request.user.id
        # _app = App.objects.get(sys_user_id = request.user.id)
        # return qs.filter(app_id = _app.id)

admin.site.register(News,NewsAdmin)