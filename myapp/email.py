from random import Random # 用于生成随机码 
from django.core.mail import send_mail # 发送邮件模块
from .models import EmailVerifyRecord # 邮箱验证model
from web.settings import EMAIL_FROM # setting.py添加的的配置信息

# 生成随机字符串
def random_str(randomlength):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0, length)]
	return str

def send_register_email(email, send_type="register"):
	email_record = EmailVerifyRecord()
	# 将给用户发的信息保存在数据库中
	code = random_str(26)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()
# 初始化为空
	email_title = "謝謝您註冊我們大資盃的會員!"
	email_body = "Email已寄送成功，請至Email內點擊連結驗證信箱，"
	# 如果为注册类型
	if send_type == "register":
		email_title = "請點擊註連結完成驗證"
		email_body = "請點擊註冊連結完成驗證:http://52.194.227.215:8000/active/{}/".format(code)
		send_status=send_mail(email_title,email_body,EMAIL_FROM,[email], fail_silently=True)
		if send_status:
			pass
	elif send_type=='forget':
		email_title = '請點擊連結完成驗證'
		email_body = '請點擊連結來修改密碼:http://52.194.227.215:8000/reset/{}/'.format(code)
		# 发送邮件
		send_status = send_mail(email_title, email_body, EMAIL_FROM, [email], fail_silently=True)
		if send_status:
			pass
