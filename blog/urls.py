from django.contrib import admin
from django.urls import path, re_path
from . import views
from . import views_cbv

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    path('cbv/news/', views_cbv.post_new),
]
