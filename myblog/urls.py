from django.conf.urls import re_path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', views.first_page ,name="first_page"),
    re_path(r'^post/(?P<post_id>\d+)/$', views.specific_post ,name="specific_post"),
    re_path(r'^post/comment/reply/(?P<comment_id>\d+)/$', views.comment ,name="comment_reply"),
    re_path('^new_post/$', views.new_post ,name="new_post"),
    re_path('^edit_post/(?P<post_id>\d+)/$', views.edit_post ,name="edit_post"),
    re_path(r'^edit/s_post/delete_comment/(?P<comment_id>\d+)/$', views.delete_comment ,name="delete_comment"),
    re_path(r'^edit/s_post/comment/delete_reply/(?P<reply_id>\d+)/$', views.delete_reply ,name="delete_reply"),
    re_path(r'^delete/post/(?P<post_id>\d+)/$', views.delete_post ,name="delete_post"),
    re_path('^posts/$', views.all_post ,name="all_post"),
    re_path('^setting/$', views.setting ,name="settings"),
    re_path('^logout_admin/$', views.logout_user ,name="logout_user"),
    re_path('^signup/$', views.signup, name='signup'),
    re_path('^logout/$', views.logout , name='logout'),
    re_path('^login/$', views.user_login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
