
from django.conf.urls import include, url
from django.contrib import admin
from CoderBlog import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
 	url(r'^comment/', include('comments.urls')),   
 	url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
]
