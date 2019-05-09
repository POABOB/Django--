#coding = utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
from hashlib import sha1
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import LoginForm, RegisterForm, ForgetForm, TeamForm, AddMemberForm, upload_paidForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,logout, login as dj_login
from django.conf import settings
from django.views.generic.base import View
from .email import send_register_email
from django.contrib.auth.decorators import login_required
from django.db import models
import os
from django.utils import timezone
# Create your views here.
#---------------------------------------------
#這是其他東西
#---------------------------------------------
def pylinkweb(request):
    return HttpResponse("Django好棒!")

def deposits(request):
	return render(request,'E_10_1.html',{})

def result(request):
	pv = int(request.GET['amount'])
	i = float(request.GET['rate'])
	n = int(request.GET['period'])
	fv = str((pv * ((1 + i)**n)))
	return HttpResponse(fv)

#--------------------------------------------
#純粹頁面顯示
#--------------------------------------------

def explain(request):
	return render(request,'user/explain.html')

def ann(request):
	return render(request,'ann.html')

def main_doc(request):
	return render(request,'main_doc.html')

def bad_doc(request):
	return render(request,'bad_doc.html')

def pre(request):
	return render(request,'pre.html')

def reg_status(request):
	team = Team.objects.filter(is_active=1)

	team_check_ok = Team.objects.filter(is_active=1, is_paid=1, is_pass=1, is_check=1)
	team_check_ok = len(team_check_ok)
	team_be_check = Team.objects.filter(is_active=1, is_pass=0)
	team_be_check = len(team_be_check)
	return render(request,'reg_status.html',{'team':team,'team_check_ok':team_check_ok, 'team_be_check':team_be_check})

def view_teams(request):
	return render(request,'view_teams.html')

def bad(request):
	return render(request,'bad.html')

def q_a(request):
	return render(request,'q_a.html')

def traffic(request):
	return render(request,'traffic.html')

def stay(request):
	return render(request,'stay.html')

def food(request):
	return render(request,'food.html')

def insurance(request):
	return render(request,'insurance.html')

def donate(request):
	return render(request,'donate.html')

#----------------------------------------------------------
#報名應用
#----------------------------------------------------------
def main(request):
	team = Team.objects.filter(not_active = 1)
	team1 = Team.objects.filter(is_pass = 1)
	team = len(team)
	team1 = len(team1)
	if "email" in request.session:
		return render(request,'user/main.html',{'team':team, 'team1':team1})
	else:
		return redirect("/user/login/")

def join(request):
	if "email" in request.session:
		now = datetime.now()
		if (datetime(2018,12,18,23,59,59) - now).total_seconds() <= 0:
			date = 0
		else:
			date = 1
		team = Team.objects.filter(email = request.session["email"], is_active = 0)
		team_n = Team.objects.filter(email = request.session["email"])
		teamNum1 = len(team_n)
		teamNum2 = len(team)

		if request.method == 'POST':
			form = TeamForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				TeamName = cd['隊伍名稱']
				team1 = Team.objects.filter(TeamName = TeamName)
				if(len(team1) == 1):
					return HttpResponse("此隊名也被使用，請在原隊名加上B!")
				elif(len(team) >= 2):
					return HttpResponse("每所學校最多只能報名兩隊!")
				else:
					team = Team()
					team.TeamName = TeamName
					team.email = request.session["email"]
					team.save()
					message = "新增隊名成功，"
					message_url = "/user/join/"
					return render(request,'pageJump.html',{'message':message,'message_url':message_url})
		else:
			form = TeamForm()
		return render(request, 'user/join.html', {'form': form, 'team':team, 'teamNum1': teamNum1 ,'date':date,'teamNum2':teamNum2})
	else:
		return redirect("/user/login/")

def DeleteTeam(request, ids):
	if "email" in request.session:
		team = Team.objects.get(email = request.session["email"], id=ids)
		team.delete()
		message = "刪除成功，"
		message_url = "/user/join/"
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		return redirect("/user/login/")



def AddMember(request, ids):
	if "email" in request.session:
		team = Team.objects.get(email = request.session["email"], id=ids)

		if(team.is_active == 1):
			return redirect("/user/login/")

		teamM = TeamMember.objects.filter(TeamName_id=ids)
		teamNum = len(teamM)

		if request.method == 'POST':
			form = AddMemberForm(request.POST, request.FILES)
			if form.is_valid():
				cd = form.cleaned_data
				TeamName_id = ids
				name = cd['名字']
				std_id = cd['學號']
				birthday = cd['生日']
				is_PE = cd['是否為體保生']
				is_foreign = cd['是否為外籍生']
				id_number = cd['身分證字號']
				cellphone = cd['手機號碼']
				if(teamNum > 0):
					position = '隊員'
				else:
					position = '隊長'
				team_check = TeamMember.objects.filter(TeamName_id=ids, std_id = std_id)
				if(len(team_check) == 1):
					return HttpResponse("學生證號碼不能相同!")
				team_check = TeamMember.objects.filter(TeamName_id=ids, id_number = id_number)
				if(len(team_check) == 1):
					return HttpResponse("身分證號碼不能相同!")
				team_check = TeamMember.objects.filter(TeamName_id=ids, cellphone = cellphone)
				if(len(team_check) == 1):
					return HttpResponse("手機號碼不能相同!")
				pic_1 = request.FILES.get('大頭照')
				pic_2 = request.FILES.get('學生證正面')
				pic_3 = request.FILES.get('學生證反面')
				pic_4 = request.FILES.get('第二證件正面')

				if pic_1.size > 2000000:
					return HttpResponse("大頭照圖片過大")
				elif pic_2.size > 2000000:
					return HttpResponse("學生證(正)圖片過大")
				elif pic_3.size > 2000000:
					return HttpResponse("學生證(反)圖片過大")
				elif pic_4.size > 2000000:
					return HttpResponse("身分證圖片過大")

				if pic_1 and pic_2 and pic_3 and pic_4 is not None:
					type_list = ['.jpg','.png']
					#判斷上傳圖片格式
					n1 = os.path.splitext(pic_1.name)[1].lower()
					n2 = os.path.splitext(pic_2.name)[1].lower()
					n3 = os.path.splitext(pic_3.name)[1].lower()
					n4 = os.path.splitext(pic_4.name)[1].lower()
					if n1 and n2 and n3 and n4 in type_list:
						member = TeamMember()
						pic_1.name = str(request.session["email"])+str(datetime.now())+'_1'+n1
						pic_2.name = str(request.session["email"])+str(datetime.now())+'_2'+n2
						pic_3.name = str(request.session["email"])+str(datetime.now())+'_3'+n3
						pic_4.name = str(request.session["email"])+str(datetime.now())+'_4'+n4
						
						member.member = name
						member.std_id = std_id
						member.birthday = birthday
						member.is_PE = is_PE
						member.is_foreign = is_foreign
						member.id_number = id_number
						member.cellphone = cellphone
						member.position = position
						member.pic_1 = pic_1
						member.pic_2 = pic_2
						member.pic_3 = pic_3
						member.pic_4 = pic_4
						member.TeamName_id = ids
						member.save()
						team1 = Team.objects.get(id=ids)
						team1.memberNum = teamNum + 1
						team1.save()
						message = "新增成功，"
						message_url = "/user/addmember/"+ids+"/"
						return render(request,'pageJump.html',{'message':message,'message_url':message_url})
					else:
						return HttpResponse("請傳jpg或png圖檔!")
		else:
			form = AddMemberForm()
		return render(request, 'user/addmember.html', {'form': form,'team':team,'teamM':teamM, 'teamNum':teamNum})
	else:
		return redirect("/user/login/")
def AddMemberCheck(request, ids):
	if "email" in request.session:
		
		team = Team.objects.filter(email = request.session["email"], id=ids)
		team.update(is_active = 1)
		team.update(active_time = datetime.now())
		team1 = TeamMember.objects.filter(TeamName_id=ids)
		team1.update(reg_time = datetime.now())
		team1.update(is_active = 1)

		message = "隊伍報名成功，"
		message_url = "/user/addmember/"+ids+"/"
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		return redirect("/user/login/")

def deleteMember(request, ids):
	if "email" in request.session:
		team1 = TeamMember.objects.get(id=ids)
		team_id = team1.TeamName_id
		team1.delete()

		message = "隊員刪除成功，"
		message_url = "/user/addmember/"+str(team_id)+"/"
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		return redirect("/user/login/")


def check(request, ids):
	if "email" in request.session:
		team = Team.objects.get(email = request.session["email"], id=ids)
		#team = team.teamname
		team1 = TeamMember.objects.filter(TeamName_id=ids)
		return render(request,'teamview.html',{'team':team,'team1':team1})
	else:
		return redirect("/user/login/")

def upload_paid(request, ids):
	if "email" in request.session:
		if request.method == 'POST':
			form = upload_paidForm(request.POST, request.FILES)
			if form.is_valid():
				upload_paid = request.FILES.get('繳費照')
				if upload_paid.size > 2000000:
					return HttpResponse("繳費照圖片過大")
				if upload_paid is not None:
					type_list = ['.jpg','.png']
					#判斷上傳圖片格式
					n1 = os.path.splitext(upload_paid.name)[1].lower()

					if n1 in type_list:
						upload_paid.name = str(request.session["email"])+str(datetime.now())+'_1'+n1
						team1 = Team.objects.get(id=ids)
						team1.upload_paid = upload_paid
						team1.save()
						message = "新增照片成功，"
						message_url = "/user/check/"+ids+"/"
						return render(request,'pageJump.html',{'message':message,'message_url':message_url})
					else:
						return HttpResponse("請傳jpg或png圖檔!")
		else:
			form = upload_paidForm()
		return render(request, 'user/upload_paid.html', {'form': form})
	else:
		return redirect("/user/login/")

def upload_paid_delete(request, ids):
	if "email" in request.session:
		team = Team.objects.filter(id=ids)
		team.update(upload_paid = None)
		message = "刪除照片成功，"
		message_url = "/user/check/"+ids+"/"
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		return redirect("/user/login/")
def myteam(request):
	if "email" in request.session:
		team = Team.objects.filter(email = request.session["email"])
		# team1 = Team.objects.get(email = request.session["email"])
		# upload_paid_len = len(team1.upload_paid)
		return render(request,'user/myteam.html',{'team':team})
	else:
		return redirect("/user/login/")
#----------------------------------------------------------
#首頁
#----------------------------------------------------------
def index(request):
	posts = Post.published.all()[:5]
	return render(request,'index.html',{'posts':posts})

#----------------------------------------------------------
#顯示公告在ann上
#----------------------------------------------------------
def post_list(request):
	posts = Post.published.all()
	paginator = Paginator(posts, 5) # 5 posts in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)
	return render(request,'post/list.html',{'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,status='published',publish__year = year,)
	return render(request,'post/detail.html',{'post': post})

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 5
	template_name = 'post/list.html'
#----------------------------------------------------------
#login測試
#----------------------------------------------------------
def login(request):
	if "email" in request.session:
		return redirect('/user/main/')
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				password = cd['密碼']
				email = cd['email']
				s1 = sha1()
				s1.update(password.encode("utf-8"))
				password = s1.hexdigest()
				user1 = authenticate(username=email,password=cd['密碼'])
				user = UserInfo.objects.filter(email = email,password = password)
				if len(user) == 1:
					#user = UserInfo.objects.get(email=cd['email'])
					if user[0].status is 1:
						user = UserInfo.objects.get(email = email,password = password)
						#dj_login(request,user)
						request.session['email'] = email
						user = UserInfo.objects.filter(email = email,password = password)
						user.update(last_login = datetime.now())
						message = "登入成功，"
						message_url = "/user/main/"
						return render(request,'pageJump.html',{'message':message,'message_url':message_url})
					else:
						return render(request,'user/emailNotVerified.html',{'email':email})
				else:
					message = "帳號或密碼錯誤,"
					message_url = "/user/login/"
					return render(request,'pageJump.html',{'message':message,'message_url':message_url})
		else:
			form = LoginForm()
		return render(request, 'user/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		user_form = RegisterForm(request.POST)
		if user_form.is_valid():
			cd = user_form.cleaned_data
			email = cd["email"]
			password = cd["密碼"]
			passconf = cd["密碼確認"]
			name = cd["真實姓名"]
			school = cd["學校"]
			department = cd["科系"]
			cellphone = cd["手機"]
			#判斷Email和手機是否重複
			check1 = UserInfo.objects.filter(email = email)
			check2 = UserInfo.objects.filter(cellphone = cellphone)
			if len(check1) == 1:
				return HttpResponse("Email已經存在了，請返回上一頁重新輸入!")
			elif len(check2) == 1:
				return HttpResponse("手機已經存在了，請返回上一頁重新輸入!!")
			else:
				#加密
				s1 = sha1()
				s1.update(password.encode("utf-8"))
				password_sha1 = s1.hexdigest()
				#建立該對象
				user = UserInfo()
				user.email = email
				user.password = password_sha1
				user.name = name
				user.school = school
				user.department= department
				user.cellphone= cellphone
				user.save()
				user1 = User.objects.create_user(username=email,password=cd["密碼"])
				user1.is_active = 0
				user1.save()
				send_register_email(email, "register")
				message='註冊成功，請到信箱找找驗證信，'
				message_url = '/user/login/'
				return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		user_form = RegisterForm()
	return render(request,'user/register.html',{'user_form': user_form})

def logout(request):
	if "email" in request.session:
		request.session.clear()
		return render(request, 'user/logout.html')
	else:
		return redirect("/")

def forget(request):
	if request.method == 'POST':
		form = ForgetForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			email = cd["Email"]
			cellphone = cd["手機"]
			#建立該對象
			user = UserInfo.objects.filter(email = email,cellphone = cellphone)
			if len(user) == 1:
				send_register_email(email, "forget")
				message='Email已寄送成功，請至Email內點擊連結驗證信箱，'
				message_url = '/'
				return render(request,'pageJump.html',{'message':message,'message_url':message_url})
			else:
				return HttpResponse('Email或手機輸入錯誤!')
	else:
		form = ForgetForm()
	return render(request,'user/forget.html',{'form': form})

def send_again(request):
	if request.method == 'POST':
		email = request.POST.get('Email')
		print(email)
		send_register_email(email, "register")
		message='Email已寄送成功，請至Email內點擊連結驗證信箱，'
		message_url = '/'
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		message='Email已寄送失敗，請聯絡網站管理員，'
		message_url = '/'
		return render(request,'pageJump.html',{'message':message,'message_url':message_url})

class ActiveUserView(View):
    def get(self, request, active_code):
        # 用code在数据库中过滤处信息
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserInfo.objects.get(email = email)
                user.status = 1
                user.save()
                user1 = User.objects.get(username = email)
                user1.is_active =1
                user1.save()

            EmailVerifyRecord.objects.filter(email=email).delete()
            message='驗證成功，'
            message_url='/user/login/'
            return render(request,'pageJump.html',{'message':message,'message_url':message_url})
        else:
            message='驗證失敗，請重新驗證一次，'
            message_url = '/'
            return render(request,'pageJump.html',{'message':message,'message_url':message_url})
        return redirect("/")


class ResetView(View):
	def get(self,request,active_code):
		record=EmailVerifyRecord.objects.filter(code=active_code)
		print(record)
		if record:
			for i in record:
				email=i.email
				is_register=UserInfo.objects.filter(email=email)
			if is_register:
				return render(request,'pass_reset.html',{'email':email})
		return redirect('/')


def ModifyView(request):
	if request.method == 'POST':
		pass1=request.POST.get('pass1','')
		pass2=request.POST.get('pass2','')
		email=request.POST.get('Email','')

		if email is None:
			return redirect('/')
		else:
			if pass1!=pass2:
				return render(request,'pass_reset.html',{'msg':'● 兩個密碼不相同！'})
			else:
				user = UserInfo.objects.get(email=email)
				s1 = sha1()
				s1.update(pass1.encode("utf-8"))
				password_sha1 = s1.hexdigest()
				user.password = password_sha1
				user.save()

				user1 = User.objects.get(username=email)
				user1.set_password(pass1)
				user1.save()
				user_letter = EmailVerifyRecord.objects.get(email=email)
				user_letter.delete()
				message='密碼修改成功，'
				message_url = '/'
				return render(request,'pageJump.html',{'message':message,'message_url':message_url})
	else:
		return redirect('/')

def realTeamMember(request):
	team = TeamMember.objects.filter(is_active=1,is_pass=1,is_paid=1,is_check=1)
	member = RealTeamMember()
	for i in team:
		member.member = i.name
		member.std_id = i.std_id
		member.birthday = i.birthday
		member.is_PE = i.is_PE
		member.is_foreign = i.is_foreign
		member.id_number = i.id_number
		member.cellphone = i.cellphone
		member.position = i.position
		member.pic_1 = i.pic_1
		member.pic_2 = i.pic_2
		member.pic_3 = i.pic_3
		member.pic_4 = i.pic_4
		member.TeamName_id = i.TeamName_id
		member.save()
		team1 = Team.objects.get(id=ids)
		team1.memberNum = teamNum + 1
		team1.save()
	return redirect('/user/view_teams/')
