from django.conf.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^(?P<user>\w+)/$', views.first_page ,name="first_page"),
    re_path('^(?P<user>\w+)/Remove_User/$', views.delete_account , name='delete_account'),
    re_path(r'^(?P<user>\w+)/post/(?P<post_id>\d+)/$', views.specific_post ,name="specific_post"),
    re_path(r'^(?P<user>\w+)/post/comment/reply/(?P<comment_id>\d+)/$', views.comment ,name="comment_reply"),
    re_path('^(?P<user>\w+)/new_post/$', views.new_post ,name="new_post"),
    re_path('^(?P<user>\w+)/edit_post/(?P<post_id>\d+)/$', views.edit_post ,name="edit_post"),
    re_path(r'^(?P<user>\w+)/edit/s_post/delete_comment/(?P<comment_id>\d+)/$', views.delete_comment ,name="delete_comment"),
    re_path(r'^(?P<user>\w+)/edit/s_post/comment/delete_reply/(?P<reply_id>\d+)/$', views.delete_reply ,name="delete_reply"),
    re_path(r'^(?P<user>\w+)/delete/post/(?P<post_id>\d+)/$', views.delete_post ,name="delete_post"),
    re_path('^(?P<user>\w+)/posts/$', views.all_post ,name="all_post"),
    re_path('^(?P<user>\w+)/setting/$', views.setting ,name="settings"),
    re_path('^user/signup/$', views.signup, name='signup'),
    re_path('^user/logout/$', views.logout_user , name='logout'),
    re_path('^$', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
