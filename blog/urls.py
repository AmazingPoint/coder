from django.conf.urls import patterns, url
from blog import views, wx_views

print "This is url!!!!!!!!!!!!!"

urlpatterns = patterns('',	
	url(r'^$', views.index, name="index"),
	url(r'^edit/(?P<articel_id>\d+)/$', views.edit, name="edit"),
	url(r'^articel/(?P<articel_id>\d+)/$', views.articel, name="articel"),
	url(r'^meta/(?P<meta_id>\d+)/$', views.meta, name="meta"),
	url(r'^home/(?P<user_id>\d+)/$', views.home, name="home"),
	url(r'^home/(?P<user_id>\d+)/(?P<meta_id>\d+)/$', views.metaown, name="metaown"),
	url(r'^del/(?P<articel_id>\d+)/$', views.delete, name="del"),
	url(r'^save/', views.save, name="save"),
	url(r'^create/', views.create, name="create"),
	url(r'^login/', views.login, name="login"),
	url(r'^loadmore/$', views.loadmore, name="loadmore"),
	url(r'^search/$', views.search, name="search"),
	url(r'^metas/$', views.metas, name="metas"),
	url(r'^dologin/$', views.dologin, name="dologin"),
	url(r'^regist/$', views.regist, name="regist"),
	url(r'^doregist/$', views.doregist, name="doregist"),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'blog/logout.html'}),
	url(r'^setpay/$', views.set_pay, name="setpay"),
	url(r'^pay/(?P<author_id>\d+)/$', views.pay, name="pay"),
	url(r'^uploadimg/$', views.upload_img, name="uploadimg"),
)

urlpatterns += patterns ('',
	url(r'^callback/$',wx_views.callback, name="callback"),
)
