# -*- coding:utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from django.http import HttpResponse
from comments.models import Comment 
from django.core import serializers
from django.template.loader import get_template 
from django.template import Context 
from mail import mail_sender
from blog.models import Articel

def load_comment(request):
	target_type = request.POST['type']
	target_id = request.POST['tid']
	print target_id
	comment_list = Comment.objects.filter(target_type=target_type).filter(target_id=target_id)
	t = get_template('comments/comment.html')
	if len(comment_list) == 0:
		html = t.render(Context({"tid": target_id},))
	else:
		html = t.render(Context({"comment_list" : comment_list},))
	return HttpResponse(html)

def add_comment(request):
	target_type = request.POST['type']
	target_id = request.POST['tid']
	content = request.POST['content']
	reply_id = request.POST['reply_id']
	reply_id = int(reply_id)
	target_id = int(target_id)
	from_user = request.user
	if from_user.is_anonymous():
		return HttpResponse('403')
	if reply_id == -1:
		comment = Comment(target_id=target_id, target_type=target_type, content=content, from_user=from_user)
	else:
		reply = Comment.objects.get(id=reply_id)
		comment = Comment(target_id=target_id, target_type=target_type, content=content, from_user=from_user, reply=reply)
	comment.save()
	receiver = Articel.objects.get(id=target_id).author.email
	target_id = str(target_id)
	sem = mail_sender.SendMail()
	sem.comment_notify(receiver, from_user.username, content, target_id)
	return HttpResponse('304')