from django.contrib import admin
from django.urls import include, path, re_path
from . import views, views_cbv

app_name = 'dojo'
urlpatterns = [
    re_path(r'^new/$', views.post_new),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit),
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    re_path(r'^list1/$', views.post_list1),
    re_path(r'^list2/$', views.post_list2),
    re_path(r'^list3/$', views.post_list3),
    re_path(r'^excel/$', views.excel_download),
    re_path(r'^cbv/list1/$', views_cbv.post_list1),
    re_path(r'^cbv/list2/$', views_cbv.post_list2),
    re_path(r'^cbv/list3/$', views_cbv.post_list3),
    re_path(r'^cbv/excel/$', views_cbv.excel_download),
]
