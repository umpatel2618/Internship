from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include

app_name= 'music'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetaiView.as_view(), name="detail"),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # path('music/<int:album_id>/', views.detail, name="detail")
    # url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name="favorite"),
]