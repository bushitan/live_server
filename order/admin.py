#coding:utf-8
from django.contrib import admin
from models import *
# Register your models here.

class CostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cost,CostAdmin)

class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(Member,MemberAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order,OrderAdmin)

class DiscountTemplateAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiscountTemplate,DiscountTemplateAdmin)

class DiscountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Discount,DiscountAdmin)
