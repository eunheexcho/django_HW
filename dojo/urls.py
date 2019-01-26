from django.contrib import admin
from django.urls import include, path
from .import views

app_name = 'dojo'
urlpatterns = [
    path('views/', views.mysum),
]