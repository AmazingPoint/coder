#coding: utf-8  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import smtplib  
from email.mime.text import MIMEText  

# #################################################
# author		:	@大妖
# pub_date	:	2015-7-27
# modify_date:	2015-7-27
# discipt	:	读取远程数据库表
# 				写入到python文件同级目录(car.xls)
# 				读取本地同级目录下收件人列表(maillist.txt)
# 				发送邮件
# ##################################################

class SendMail:
	'''发送邮件'''
	def welcom_register(self, receiver,user):
		sender = '2715657947@qq.com'  
		receiver = receiver 
		subject = 'CODER 程序员的技术社区'  
		smtpserver = 'smtp.qq.com'  
		username = '2715657947@qq.com'  
		password = '99delove'  


		content="<html><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/><head><title>CODER 程序员的技术社区</title><style type='text/css'>p{margin:20px 10px; color:#aaa; font-size: 14px;} table{border-top: #339966 6px solid;  padding: 30px 0;} td{padding: 20px 0; }</style></head><body><table style='text-align:center; width:80%; margin:auto;' ><tr><td style='border-bottom: 4px solid #ccc;'><h1 style='color:#339966;'>Coder</h1></td></tr><tr><td><p>感谢您的注册和支持。<p><p>Coder是一个程序员社区，你可以在这里找到自己的天地。</p><p>Coder目前还正在开发状态，但Coder会对每一个用户负责。</p></td></tr><tr style='background-color:#eee;'><td style='font-size:13px; border-bottom:20px solid #eee;'>联系方式:<a style='color:#339966;' href='mailto:greenpointan@icloud.com'>greenpointan@icloud.com</a></td></tr></table></body></html>"
		msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
		msg["Accept-Language"]="zh-CN"
		msg["Accept-Charset"]="ISO-8859-1,utf-8"
		msg['From'] = sender 
		msg['To'] = receiver

		smtp = smtplib.SMTP()
		smtp.connect(smtpserver)
		smtp.set_debuglevel(1)
		smtp.login(username, password)  
		smtp.sendmail(sender, receiver, msg.as_string()) 
		smtp.close()

	def comment_notify(self, receiver, from_user, contents ,target_id):
		sender = '2715657947@qq.com'  
		receiver = receiver 
		smtpserver = 'smtp.qq.com'  
		username = '2715657947@qq.com'  
		password = '99delove'  

		content="<html><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/><head><title>CODER 程序员的技术社区</title><style type='text/css'>p{margin:20px 10px; color:#aaa; font-size: 14px;} table{border-top: #339966 6px solid;  padding: 30px 0;} td{padding: 20px 0; }</style></head><body><table style='text-align:center; width:80%; margin:auto;' ><tr><td style='border-bottom: 4px solid #ccc;'><h1 style='color:#339966;'>Coder</h1></td></tr><tr><td><p>您在coder上的文章有新的动态。</p><b>"+ from_user  +"</b>评论了您的文章 <a href='http://123.57.149.136/articel/"+ target_id +"'> http://123.57.149.136/articel/"+ target_id +"</a><p><b>"+ contents +"</b></p></td></tr><tr style='background-color:#eee;'><td style='font-size:13px; border-bottom:20px solid #eee;'>联系方式:<a style='color:#339966;' href='mailto:greenpointan@icloud.com'>greenpointan@icloud.com</a></td></tr></table></body></html>"
		msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
		msg["Accept-Language"]="zh-CN"
		msg["Accept-Charset"]="ISO-8859-1,utf-8"
		msg['From'] = sender 
		msg['To'] = receiver

		smtp = smtplib.SMTP()	
		smtp.connect(smtpserver)
		smtp.set_debuglevel(1)
		smtp.login(username, password)  
		smtp.sendmail(sender, receiver, msg.as_string()) 
		smtp.close()


	