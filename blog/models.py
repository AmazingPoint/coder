# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CustomProFile(models.Model):
	'''User ProFile'''
	user = models.ForeignKey(User, related_name='user_up', verbose_name='用户')
	weichat_pay = models.ImageField("微信付款码", upload_to = 'pay_photos', blank=True, null=True)
	class Meta:
		verbose_name_plural = '个人信息'

class ITMeta(models.Model):
	'''The meta for IT '''
	name = models.CharField('名称', max_length=48)
	is_active = models.BooleanField(default=True)
	class Meta:
		verbose_name_plural = '技术标签'
	def __unicode__(self):
		return self.name


class Articel(models.Model):
	'''The Articel wrote by coder'''
	headline = models.CharField('标题', max_length=100)
	pub_date = models.DateTimeField('发布时间', default=timezone.now)
	meta = models.ManyToManyField(ITMeta, verbose_name='技术标签', related_name='articel_meta')
	content = models.TextField('文章内容')
	is_pub = models.BooleanField(default=False)
	author = models.ForeignKey(User, verbose_name="作者")
	vnumber = models.IntegerField('浏览次数',default=0)
	class Meta:
		verbose_name_plural = '文章'
	def __unicode__(self):
		return self.headline