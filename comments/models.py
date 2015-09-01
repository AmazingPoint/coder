# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
	'''comment model'''
	target_type = models.CharField('目标类型', max_length=48)
	target_id = models.IntegerField('目标ID')
	reply = models.ForeignKey('self', related_name='comment_reply', verbose_name='回复目标', null=True)
	content = models.TextField('内容', max_length=1024)
	from_user = models.ForeignKey(User, related_name='comment_user', verbose_name='评论者')
	pud_date = models.DateTimeField('评论时间', default=timezone.now)
	class Meta:
		verbose_name_plural = '评论'
	def __unicode__(self):
		return self.content