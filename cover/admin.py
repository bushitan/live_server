#coding:utf-8
from django.contrib import admin
from models import *
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag,TagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article,ArticleAdmin)

class ImageLibraryAdmin(admin.ModelAdmin):
    pass
admin.site.register(ImageLibrary,ImageLibraryAdmin)
class NewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(News,NewsAdmin)