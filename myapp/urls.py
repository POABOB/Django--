from django.conf.urls import url
from . import views, email
from myapp.views import ActiveUserView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/', views.login),
	url(r'^forget/', views.forget),
	url(r'^explain/', views.explain),
	url(r'^main/', views.main),
	url(r'^myteam/', views.myteam),
	url(r'^join/', views.join),
	url(r'^logout/', views.logout),
	url(r'^send_again/', views.send_again),
	url(r'^modify/',views.ModifyView,name='modify'),
	url(r'^check/(?P<ids>[0-9]+)/', views.check),
	url(r'^addmember/(?P<ids>[0-9]+)/',views.AddMember),
	url(r'^deletemember/(?P<ids>[0-9]+)/',views.deleteMember),
	url(r'^addmembercheck/(?P<ids>[0-9]+)/',views.AddMemberCheck),
	url(r'^deleteteam/(?P<ids>[0-9]+)/',views.DeleteTeam),
	url(r'^upload_paid/(?P<ids>[0-9]+)/',views.upload_paid),
	url(r'^upload_paid_delete/(?P<ids>[0-9]+)/',views.upload_paid_delete),
	url(r'^realteammember/', views.realTeamMember),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)