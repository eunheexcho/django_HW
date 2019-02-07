from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from .forms import LoginForm
from . import views


urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.login, name='login',
            kwargs={
                'authentication_form': LoginForm,
                'template_name': 'accounts/login_form.html'
            }),
    re_path(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    re_path(r'^profile/$', views.profile, name='profile'),
]
