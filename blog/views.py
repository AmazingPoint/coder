# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, hashers
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import re
from django.core import serializers
from django.template.loader import get_template 
from django.template import Context 
from mail_sender import SendMail
import time

@login_required(login_url="/login/")
def home(request, user_id):
	meta_list = ITMeta.objects.all()
	user_id = int(user_id)
	if request.user.id == user_id:
		articel_list = Articel.objects.filter(author__id=user_id).order_by('-pub_date')[0:10]
	else:
		articel_list = Articel.objects.filter(author__id=user_id).filter(is_pub=True).order_by('-pub_date')[0:10]
	print articel_list
	return render(request, 'blog/home.html', locals())

@login_required(login_url="/login/")
def metaown(request, user_id, meta_id):
	meta_list = ITMeta.objects.all()
	articel_list = Articel.objects.filter(author__id=user_id).filter(meta__id=meta_id).order_by('-pub_date')[0:10]
	return render(request, 'blog/home.html', locals())

@login_required(login_url="/login/")
def delete(request, articel_id):
	articel = Articel.objects.get(id=articel_id)
	if request.user.id == articel.author.id:
		articel.delete()
		return HttpResponseRedirect(reverse('home', args=(request.user.id,)))
	else:
		return HttpResponse("我很懒，所以我也很穷，别黑我！")


def index(request):
	meta_list = ITMeta.objects.all()
	articel_list = Articel.objects.filter(is_pub=True).order_by('-pub_date')[0:10]
	return render(request, 'blog/index.html', locals())

def articel(request, articel_id):
	articel = Articel.objects.get(id = articel_id)
	articel.vnumber = articel.vnumber+1
	articel.save()
	return render(request, 'blog/articel.html', locals())

def loadmore(request):
	meta_name = request.GET.get('meta_name',None)
	number_start = request.GET.get('number_start',None)
	number_start = int(number_start)
	number_end = number_start + 11
	if meta_name is None:
		articel_list = Articel.objects.filter(is_pub=True).order_by('-pub_date')[number_start:number_end]
	else:	
		articel_list = Articel.objects.filter(is_pub=True).filter(meta__name=meta_name).order_by('-pub_date')[number_start:number_end]
	t = get_template('blog/articel_list.html')
	html = t.render(Context({"articel_list" : articel_list}))
	return HttpResponse(html)

def metas(request):
	metas = ITMeta.objects.all()
	return render(request, 'blog/metas.html', locals())

def meta(request, meta_id):
	meta = ITMeta.objects.get(id= meta_id)
	meta_list = ITMeta.objects.all()
	articel_list = Articel.objects.filter(is_pub=True).filter(meta=meta).order_by('pub_date')[0:10]
	return render(request, 'blog/index.html', locals())

def search(request):
	search_text = request.GET['search_text']
	articel_list = Articel.objects.filter(headline__contains=search_text)
	t = get_template('blog/articel_list.html')
	html = t.render(Context({"articel_list" : articel_list}))
	print html
	return HttpResponse(html)

@login_required(login_url="/login/")
def edit(request,articel_id):
	articel = Articel.objects.get(id = articel_id)
	if request.user.id == articel.author.id:
		metas = ITMeta.objects.all()
		return render(request, 'blog/edit.html', locals())
	else:
		return HttpResponse("我很懒，所以我也很穷，别黑我！")

@login_required(login_url="/login/")
def save(request):
	user = request.user
	id = request.POST['id']
	headline = request.POST['headline']
	content = request.POST['content']
	metas = request.POST['metas']
	print id
	articel =  Articel.objects.get(id=id)
	if metas == '':
		articel.headline= headline
		articel.content = content
		articel.author = user
		articel.is_pub = False
		articel.save()
		return HttpResponse("success")
	else:
		meta_arr = metas.split(',')
		meta_arr = list(set(meta_arr))
		for ma in meta_arr:
			if ma != '':
				articel.meta.add(ITMeta.objects.get(id=int(ma)))
		articel.is_pub = True
		articel.save()
		return HttpResponse(articel.id)
		

@login_required(login_url="/login/")
def create(request):
	user = request.user
	articel = Articel(headline="默认标题", content="##保存井号，输入标题", author=user)
	articel.save()
	return HttpResponseRedirect(reverse('edit', args=(articel.id,)))

def regist(request):
	return render(request, 'blog/register.html')

def doregist(request):
	username = request.POST.get('username', '1')
	password = request.POST.get('password', '1')
	password2 = request.POST.get('password2', '2')
	email = request.POST.get('email', '1')
	if(len(username) < 2):
		error = '用户名至少应为两个字符'
		return render(request, 'blog/register.html', locals())

	if(len(password) < 8):
		error = '密码至少应为八个字符'
		return render(request, 'blog/register.html', locals())

	if(password != password2):
		error = '请输入相同的密码'
		return render(request, 'blog/register.html', locals())

	if len(email) < 7:
		error = '请确保邮箱合法'
		return render(request, 'blog/register.html', locals()) 
	
	if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
		error = '请确保邮箱合法'
		return render(request, 'blog/register.html', locals()) 
	try:
	    user = User.objects.get(username=username)
	except User.DoesNotExist:
	    user = None
	if user is not None:
		error = '重复的用户名'
		return render(request, 'blog/register.html', locals())
	else:
		user = User.objects.create_user(username, email, password)
		user.save()
		user = User.objects.get(username=username)
		user = authenticate(username = user.username, password=password)
		auth_login(request,user)
		sm = SendMail()
		sm.send_mail(email, username)
		return home(request, user.id)


def login(request):
	return render(request,'blog/login.html')


def dologin(request):
	username = request.POST.get('username', None)
	password = request.POST.get('password', None)
	user = authenticate(username = username, password = password)
	if user is not None:
		auth_login(request,user)
		return home(request,user.id)
	else:
		error = '请检查用户名或密码'
		return render(request, 'blog/login.html', locals())