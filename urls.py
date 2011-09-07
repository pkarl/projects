from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    # (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
)
