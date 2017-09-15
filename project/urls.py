from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.contrib.auth import views

urlpatterns = [
     url(r'^groups/add', GroupCreateView.as_view(), name='group-create'),
     url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='group-delete'),
     url(r'^groups/(?P<pk>\d+)/edit/$', GroupEditView.as_view(), name='group-edit'),
     url(r'^groups/$', GroupListView.as_view(), name='group-list'),
     url(r'^groups/(?P<pk>\d+)/$', StudentListView.as_view(), name='student-list'),
     url(r'^groups/(?P<group_pk>\d+)/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='student-delete'),
     url(r'^groups/(?P<pk>\d+)/add/$', StudentCreateView.as_view(), name='student-create'),
     url(r'^groups/(?P<pk>\d+)/edit', StudentEditView.as_view(), name='student-edit'),     
     url(r'^admin/', admin.site.urls),
     url(r'^login/$', views.login, name='login'),
     url(r'^logout/$', views.logout, name='logout'),
]

