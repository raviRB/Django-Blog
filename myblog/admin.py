from django.contrib import admin
from . import models

admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.Blog_detail)
admin.site.register(models.User_Profile)
admin.site.register(models.Reply)
