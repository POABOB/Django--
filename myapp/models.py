#coding = utf-8
from django.db import models as m
from django.utils import timezone 
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html


#datetime.now(tz=timezone.utc)
# Create your models here.
#-------------------------------------------------------------------
#mysql資料
#-------------------------------------------------------------------
class UserInfo(m.Model):
    email = m.CharField(max_length = 50, verbose_name=u"Email")
    password = m.CharField(max_length = 52, verbose_name=u"密碼")
    name = m.CharField(max_length = 15, verbose_name=u"名字")
    school = m.CharField(max_length = 50, verbose_name=u"學校")
    department= m.CharField(max_length = 10, verbose_name=u"科系")
    status = m.BigIntegerField(default = 0, verbose_name=u"狀態")
    cellphone= m.CharField(max_length = 10, verbose_name=u"手機")
    last_login = m.DateTimeField(auto_now=True, verbose_name=u"上次登入時間")

    class Meta:
        verbose_name = u"會員資訊"
        verbose_name_plural = verbose_name

#-------------------------------------------------------------------
#mysql資料和獲取所有公告資料
#-------------------------------------------------------------------
class PublishedManager(m.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')

class Post(m.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = m.CharField(max_length=250, verbose_name=u"標題")
    slug = m.SlugField(max_length=250,
                            unique_for_date='publish', verbose_name=u"標題索引")
    author = m.ForeignKey(User,
                                related_name='blog_posts', on_delete=m.CASCADE, verbose_name=u"發佈者")
    body = m.TextField(verbose_name=u"內文")
    publish = m.DateTimeField(default=timezone.now, verbose_name=u"發佈時間")
    created = m.DateTimeField(auto_now_add=True, verbose_name=u"創建時間")
    updated = m.DateTimeField(auto_now=True, verbose_name=u"更新時間")
    status = m.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft', verbose_name=u"狀態")
                            
    class Meta:
        ordering = ('-publish',)
        verbose_name = u"公告"
        verbose_name_plural = verbose_name
		
    def __str__(self):
        return self.title


    objects = m.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])

#-------------------------------------------------------------------
#Admin後台檢索資料
#-------------------------------------------------------------------
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    



class PostUserInfo(admin.ModelAdmin):
    list_display = ('email','name','school','department','status','cellphone')
    list_filter = ('name','school')
    search_fields = ('email', 'name','school',)
    raw_id_fields = ('name',)


#-------------------------------------------------------------------
#Email寄送驗證碼
#-------------------------------------------------------------------
class EmailVerifyRecord(m.Model):
    # 驗證碼
    code = m.CharField(max_length=100, verbose_name=u"驗證碼")
    email = m.EmailField(max_length=50, verbose_name=u"Email")
    # 註冊驗證和回驗證
    send_type = m.CharField(verbose_name=u"驗證碼類型", max_length=10, choices=(("register",u"註冊"), ("forget",u"找回密碼")))
    send_time = m.DateTimeField(verbose_name=u"發送時間", auto_now=True)
    class Meta:
        verbose_name = u"Email驗證碼"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

#-------------------------------------------------------------------
#隊伍
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#隊伍成員及資料
#-------------------------------------------------------------------
class Team(m.Model):
    TeamName = m.CharField(max_length=10, unique=True, verbose_name=u"隊伍名稱")
    memberNum = m.IntegerField(default = 0, verbose_name=u"隊員人數")
    not_active = m.IntegerField(default = 1, verbose_name=u"是否提交隊名")
    is_active = m.IntegerField(default = 0, verbose_name=u"是否提交隊員資料")
    is_check = m.IntegerField(default = 0, verbose_name=u"是否資料確認")
    is_paid =  m.IntegerField(default = 0, verbose_name=u"是否付費")
    upload_paid =  m.ImageField(default =None ,upload_to='img/', blank=True,verbose_name=u"是否上傳付費照")
    is_pass =  m.IntegerField(default = 0, verbose_name=u"是否審核")
    email = m.EmailField(max_length=50, default = '', verbose_name=u"Email")
    active_time = m.DateTimeField(auto_now=True, verbose_name=u"報名時間")

    class Meta:
        verbose_name = u"隊伍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.TeamName


class TeamMember(m.Model):
    TeamName = m.ForeignKey(Team, on_delete=m.CASCADE, verbose_name=u"隊伍名稱")
    member = m.CharField(max_length=40, verbose_name=u"姓名")
    std_id = std_id = m.CharField(max_length=20, verbose_name=u"學號")
    birthday = m.CharField(max_length=10, verbose_name=u"生日")
    is_PE = m.IntegerField(default = 0, verbose_name=u"體保")
    is_foreign = m.IntegerField(default = 0, verbose_name=u"外籍")
    id_number = m.CharField(max_length=10, verbose_name=u"身分證")
    cellphone = m.CharField(max_length=10, verbose_name=u"手機")
    position = m.CharField(max_length=5, verbose_name=u"身分")
    pic_1 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_2 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_3 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_4 = m.ImageField(upload_to='img/',null=False,blank=False)
    is_active = m.IntegerField(default = 0, verbose_name=u"是否提交隊員資料")
    reg_time = m.DateTimeField(auto_now=True, verbose_name=u"報名時間")

    class Meta:
        verbose_name = u"隊伍成員(未審核)"
        verbose_name_plural = verbose_name

    def pic_1x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_1.url,self.pic_1.url))
    pic_1.allow_tags = True
    def pic_2x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_2.url,self.pic_1.url))
    pic_2.allow_tags = True
    def pic_3x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_3.url,self.pic_1.url))
    pic_3.allow_tags = True
    def pic_4x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_4.url,self.pic_1.url))
    pic_4.allow_tags = True

    pic_1x.short_description = u"大頭照"
    pic_2x.short_description = u"學生證正面"
    pic_3x.short_description = u"學生證正面"
    pic_4x.short_description = u"第二證件"
class RealTeamMember(m.Model):
    TeamName = m.ForeignKey(Team, on_delete=m.CASCADE, verbose_name=u"隊伍名稱")
    member = m.CharField(max_length=40, verbose_name=u"姓名")
    std_id = m.CharField(max_length=20, verbose_name=u"學號")
    birthday = m.CharField(max_length=10, verbose_name=u"生日")
    is_PE = m.IntegerField(default = 0, verbose_name=u"體保")
    is_foreign = m.IntegerField(default = 0, verbose_name=u"外籍")
    id_number = m.CharField(max_length=10, verbose_name=u"身分證")
    cellphone = m.CharField(max_length=10, verbose_name=u"手機")
    position = m.CharField(max_length=5, verbose_name=u"身分")
    pic_1 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_2 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_3 = m.ImageField(upload_to='img/',null=False,blank=False)
    pic_4 = m.ImageField(upload_to='img/',null=False,blank=False)
    is_active = m.IntegerField(default = 0, verbose_name=u"是否提交隊員資料")
    reg_time = m.DateTimeField(auto_now=True, verbose_name=u"報名時間")
    class Meta:
        verbose_name = u"隊伍成員(已審核)"
        verbose_name_plural = verbose_name

    def pic_1x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_1.url,self.pic_1.url))
    pic_1.allow_tags = True
    def pic_2x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_2.url,self.pic_1.url))
    pic_2.allow_tags = True
    def pic_3x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_3.url,self.pic_1.url))
    pic_3.allow_tags = True
    def pic_4x(self):
        return format_html('<a href="%s" target=_blank><img src="%s" width="200px" /></a>' % (self.pic_4.url,self.pic_1.url))
    pic_4.allow_tags = True


    TeamName.short_description = u"隊伍名稱"
    member.short_description = u"姓名"
    std_id.short_description = u"學號"
    birthday.short_description = u"生日"
    is_PE.short_description = u"體保"
    is_foreign.short_description = u"外籍"
    id_number.short_description = u"身分證"
    cellphone.short_description = u"手機"
    position.short_description = u"身分"
    pic_1x.short_description = u"大頭照"
    pic_2x.short_description = u"學生證正面"
    pic_3x.short_description = u"學生證正面"
    pic_4x.short_description = u"第二證件"
