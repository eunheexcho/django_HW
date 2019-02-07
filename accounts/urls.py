from django.urls import path, re_path
from .import views

urlpatterns =[
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^profile/$', views.profile)

]