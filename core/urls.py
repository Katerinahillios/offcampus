from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^place/create/$', login_required(PlaceCreateView.as_view()), name='place_create'), 
    url(r'^place/$', PlaceListView.as_view(), name='place_list'),    
    url(r'^place/(?P<pk>\d+)/$', PlaceDetailView.as_view(), name='place_detail'),
    url(r'^place/update/(?P<pk>\d+)/$', login_required(PlaceUpdateView.as_view()), name='place_update'),  
    url(r'^place/delete/(?P<pk>\d+)/$', login_required(PlaceDeleteView.as_view()), name='place_delete'),    
    url(r'^place/(?P<pk>\d+)/comment/create/$', login_required(CommentCreateView.as_view()), name='comment_create'),
    url(r'^place/(?P<place_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', login_required(CommentUpdateView.as_view()), name='comment_update'),
    url(r'^place/(?P<place_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', login_required(CommentDeleteView.as_view()), name='comment_delete'),
    url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
    url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
    url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),                   
)