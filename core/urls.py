from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^place/create/$', PlaceCreateView.as_view(), name='place_create'), 
    url(r'^place/$', PlaceListView.as_view(), name='place_list'),    
    url(r'^place/(?P<pk>\d+)/$', PlaceDetailView.as_view(), name='place_detail'),
    url(r'^place/update/(?P<pk>\d+)/$', PlaceUpdateView.as_view(), name='place_update'),  
    url(r'^place/delete/(?P<pk>\d+)/$', PlaceDeleteView.as_view(), name='place_delete'),    
    url(r'^place/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
    url(r'^place/(?P<place_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', CommentUpdateView.as_view(), name='comment_update'),                          
)