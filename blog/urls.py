from django.urls import re_path, path
from blog import views_cbv
from blog.views import post_edit
from .import views

urlpatterns = [
    re_path(r'^$', views_cbv.post_list, name='post_list'),
    path('<int:pk>/', views_cbv.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', post_edit, name='post_edit'),
    path('cbv/new/', views_cbv.post_new),
    path('cbv/<int:pk>/edit', views_cbv.post_edit),
    path('cbv/<int:pk>/delete', views_cbv.post_delete),

]