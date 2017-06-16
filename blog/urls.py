from django.conf.urls import url
from blog import views
from blog.views import post_list

urlpatterns = [
    url(r'^blog/$', post_list),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
]
