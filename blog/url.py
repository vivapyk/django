from django.urls import re_path, path
from blog import views_cbv
from .import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),

    path('cbv/new/', views_cbv.post_new),
]