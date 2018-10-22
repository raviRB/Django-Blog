from django.conf.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', views.first_page ,name="first_page"),
    re_path(r'^post/(?P<post_id>\d+)/$', views.specific_post ,name="specific_post"),
    re_path(r'^post/(?P<comment_id>\d+)/$', views.comment ,name="comment_reply"),
    re_path('^new_post/$', views.new_post ,name="new_post"),
    re_path('^edit_post/(?P<post_id>\d+)/$', views.edit_post ,name="edit_post"),
    re_path('^posts/$', views.all_post ,name="all_post"),
    re_path('^setting/$', views.setting ,name="settings"),
    re_path('^logout_admin/$', views.logout_user ,name="logout_user"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
