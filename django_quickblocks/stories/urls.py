from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<type>.*)/(?P<id>\d+)/(?P<title>.*)/$', StoryView.as_view(), name="stories.story_read"),
    url(r'^(?P<type>.*)/(?P<id>\d+)/$', StoryView.as_view()),
    url(r'^(?P<type>.*)/$', StoryListView.as_view(), name="stories.story_list"),
)
