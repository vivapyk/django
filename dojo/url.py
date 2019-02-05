from django.conf.urls import url
from django.urls import path

from dojo.views import post_new, post_edit
from . import views
from . import views_cbv

urlpatterns = [
    path('new/', post_new),
    path('<int:id>', views.post_detail),
    path('<int:id>/edit/', post_edit),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    # url(r'^excel/$', views.excel_download)

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    # url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^excel/$', views_cbv.excel_download)
]