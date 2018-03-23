#coding:utf-8
from django.contrib import admin
from models import *
from live_server.settings import *
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag,TagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ( STATIC_URL + 'tinymce/tinymce.min.js',
               STATIC_URL + 'tinymce/textareas.js')
admin.site.register(Article,ArticleAdmin)

class NewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(News,NewsAdmin)