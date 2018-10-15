from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.first_page ,name="first_page"),
    re_path(r'^post/(?P<post_id>\d+)/$', views.specific_post ,name="specific_post"),
    re_path('^new_post/$', views.new_post ,name="new_post"),
    re_path('^posts/$', views.all_post ,name="all_post"),
]
