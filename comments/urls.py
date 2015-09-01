from django.conf.urls import patterns, url
from comments import views

print "comments url loaed"

urlpatterns = patterns('',
	#renturn json type
	url(r'^loadcomment/$', views.load_comment, name="loadcomment"),
	url(r'^addcomment/$', views.add_comment, name="addcomment"),
)
