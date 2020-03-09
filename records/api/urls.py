from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework import routers
from api import views

from api.routers import DefaultRouterWithSimpleViews
from api.views import  UserViewSet, FileList


router = DefaultRouterWithSimpleViews()
router.register(r'user', UserViewSet, 'user')
router.register(r'file', FileList, 'files')

urlpatterns = [
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/file/detail/(?P<pk>\d+)$', views.Detail_File.as_view()),
    
]


