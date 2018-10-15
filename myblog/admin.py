from django.contrib import admin
from . import models

admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.Blog_detail)