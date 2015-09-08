# -*- coding:utf-8 -*-

from django.http import HttpResponse

def callback(request):
	return HttpResponse("验证必然是失败的")
