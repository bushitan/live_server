#coding:utf-8
from django.contrib import admin
from models import *
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

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)
class FileLibraryAdmin(admin.ModelAdmin):
    pass
admin.site.register(FileLibrary,FileLibraryAdmin)
class FileTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(FileTag,FileTagAdmin)


class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company,CompanyAdmin)