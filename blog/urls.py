from django.conf.urls import patterns, include, url
from blog.views import PostsListView, PostDetailView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shtbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',PostsListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), 
    # url(r'^/new/$', UserListView.as_view(), name="user_list"),
    )
