"""
URL configuration for simplesocial project.

"""
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.HomePage.as_view(),name='home'),
    re_path(r'^accounts/',include('accounts.urls',namespace='accounts')),
    re_path(r'^accounts/',include('django.contrib.auth.urls')),
    re_path(r'^test/$',views.TestPage.as_view(),name='test'),
    re_path(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    re_path(r'^posts/',include('posts.urls',namespace='posts')),
    re_path(r'^groups/',include('groups.urls',namespace='groups')),
]
