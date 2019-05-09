"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views
from myapp.views import ActiveUserView, ResetView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('myapp.urls')),
    url(r'^$', views.index, name='home'),
    url(r'^ann/$', views.post_list, name='post_list'),
    url(r'^ann/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^main_doc/', views.main_doc),
    url(r'^bad_doc/', views.bad_doc),
    url(r'^pre/', views.pre),
    url(r'^reg_status/', views.reg_status),
    url(r'^view_teams/', views.view_teams),
    url(r'^bad/', views.bad),
    url(r'^q_a/', views.q_a),
	url(r'^traffic/', views.traffic),
    url(r'^stay/', views.stay),
	url(r'^food/', views.food),
    url(r'^insurance/', views.insurance),
	url(r'^donate/', views.donate),
    path(r'active/<str:active_code>/',ActiveUserView.as_view()), # 提取出active后的所有字符赋给active_code
    path(r'reset/<str:active_code>/',ResetView.as_view(),name='reset'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
