#coding:utf-8
from django.contrib import admin
from models import *
# Register your models here.

class LiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(App,LiteAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)
class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company,CompanyAdmin)