from django.contrib import admin
from .models import UserInfo, Post, EmailVerifyRecord, Team,TeamMember, RealTeamMember 
from django import forms
from django.db import models as m
# Register your models here.
#-------------------------------------------------------------------
#Admin後台檢索資料
#-------------------------------------------------------------------
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status')
    search_fields = ('title', 'body','publish')
    date_hierarchy = 'publish'
    formfield_overrides = { m.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('/static/ckeditor/ckeditor.js',)
        css = {
            'all': ('/static/ckeditor/cotents.css','/static/ckeditor/fix.css')
        }
class PostUserInfoAdmin(admin.ModelAdmin):
    list_display = ('email','name','school','department','status','cellphone','last_login')
    search_fields = ('email', 'name','school',)
    list_filter = ('email','school' ,'last_login')

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class TeamAdmin(admin.ModelAdmin):
    list_display = ('TeamName','not_active','is_active','is_paid','upload_paid','is_check','is_pass','email','memberNum','active_time')
    search_fields = ('TeamName','not_active','is_active','is_paid','upload_paid','is_check','is_pass','email','memberNum','active_time')
    list_filter = ('TeamName','not_active','is_active','is_paid','upload_paid','is_check','is_pass','email','memberNum','active_time')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','pic_1x','pic_2x','pic_3x','pic_4x','is_active','reg_time')
    search_fields = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','is_active','reg_time')
    list_filter = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','is_active','reg_time')



class RealTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','pic_1x','pic_2x','pic_3x','pic_4x','is_active')
    search_fields = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','is_active')
    list_filter = ('TeamName_id','member','std_id','birthday','is_PE','is_foreign','id_number','cellphone','position','is_active')

admin.site.register(TeamMember ,TeamMemberAdmin)
admin.site.register(RealTeamMember ,RealTeamMemberAdmin)
admin.site.register(Team ,TeamAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(UserInfo, PostUserInfoAdmin)
admin.site.register(Post, PostAdmin)
