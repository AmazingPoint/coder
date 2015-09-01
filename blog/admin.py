from django.contrib import admin
from blog.models import *
from comments.models import Comment

admin.site.register(ITMeta)
admin.site.register(Articel)
admin.site.register(Comment)
