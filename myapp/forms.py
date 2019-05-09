from django import forms
from django.contrib.auth.models import User


#----------------------------------------------------------
#登入表單
#----------------------------------------------------------
class LoginForm(forms.Form):
	email = forms.EmailField(max_length=30,required=True,error_messages={'required': 'Email不能為空!','invalid': 'Email格式錯誤!'})
	密碼 = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True,min_length=6,error_messages={'required': '密碼不能為空!', 'min_length': "最少要6個字元!",'max_length': "最多只能30個字元!"})

#----------------------------------------------------------
#寄問題表單
#----------------------------------------------------------
class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget=forms.Textarea)

#----------------------------------------------------------
#註冊表單
#----------------------------------------------------------
class RegisterForm(forms.Form):
	email = forms.EmailField(max_length=30,required=True,error_messages={'required': 'Email不能為空!','invalid': 'Email格式錯誤!'})
	密碼 = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True,
             min_length=6,
             error_messages={'required': '密碼不能為空!', 'min_length': "最少要6個字元!",'max_length': "最多只能30個字元!"})
	密碼確認 = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True,
             min_length=6,
             error_messages={'required': '密碼不能為空!', 'min_length': "最少要6個字元!",'max_length': "最多只能30個字元!"})
	真實姓名 = forms.CharField(max_length=20,required=True, error_messages={'required': '真實姓名不能為空!','max_length': "最多只能20個字元!"})
	學校 = forms.CharField(max_length=15,required=True,error_messages={'required': '學校不能為空!','max_length': "最多只能15個字元!"})
	科系 = forms.CharField(max_length=20,required=True,error_messages={'required': '科系不能為空!','max_length': "最多只能20個字元!"})
	手機 = forms.CharField(max_length=10,required=True,error_messages={'required': 'Cellphone不能為空!','max_length': "最多只能10個字元!"})

	def clean(self):
		'''判斷密碼'''
		p1=self.cleaned_data.get('密碼')
		p2=self.cleaned_data.get('密碼確認')
		if p1!=p2:
			raise forms.ValidationError('兩個密碼不相符!')
		else:
			return self.cleaned_data

#----------------------------------------------------------
#忘記密碼表單
#----------------------------------------------------------
class ForgetForm(forms.Form):
	Email = forms.EmailField(max_length=50,required=True,error_messages={'required': 'Email不能為空!','max_length': "最多只能50個字元!"})
	手機 = forms.CharField(required=True, max_length=10, error_messages={'required': '手機不能為空!', 'max_length': "最多只能10個字元!"})

#----------------------------------------------------------
#新增隊伍表單
#----------------------------------------------------------
class TeamForm(forms.Form):
	隊伍名稱 = forms.CharField(max_length=10,required=True,error_messages={'required': '隊伍名稱不能為空!','max_length': "最多只能10個字元!"})

CHOICES= [
    ('1','是'),
    ('0','否'),
    ]

class AddMemberForm(forms.Form):
	名字 = forms.CharField(max_length=20,required=True,error_messages={'required': '名字不能為空!','max_length': "最多只能20個字元!"})
	學號 = forms.CharField(max_length=20,required=True,error_messages={'required': '學號不能為空!','max_length': "最多只能20個字元!"})
	生日 = forms.CharField(max_length=10,required=True,error_messages={'required': '生日不能為空!','max_length': "最多只能10個字元!"})
	是否為體保生 = forms.ChoiceField(choices=CHOICES ,initial='0')
	是否為外籍生 = forms.ChoiceField(choices=CHOICES ,initial='0')
	身分證字號 = forms.CharField(max_length=10,required=True,error_messages={'required': '身分證字號不能為空!','max_length': "最多只能10個字元!"})
	手機號碼 = forms.CharField(max_length=10,required=True,error_messages={'required': '手機不能為空!','max_length': "最多只能10個字元!"})
	大頭照 = forms.ImageField()
	學生證正面 = forms.ImageField()
	學生證反面 = forms.ImageField()
	第二證件正面 = forms.ImageField()

class upload_paidForm(forms.Form):
	繳費照 = forms.ImageField()