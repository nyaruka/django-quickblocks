from django.contrib.auth.models import User, Group
from rapidsms_httprouter.models import Message
from django import forms

from smartmin.views import *
from django_quickblocks.models import QuickBlock, QuickBlockType
from django.http import Http404

class StoryListView(TemplateView):

    def get_template_names(self):
        return ['stories/%s_list.html' % self.type.slug, 'stories/list.html']

    def get_context_data(self,  **kwargs):
        if 'type' in kwargs:
            self.type = QuickBlockType.objects.get(slug=kwargs['type'])
            stories = QuickBlock.objects.filter(is_active=True,
                                                quickblock_type=self.type).order_by('-priority')
            return dict(stories=stories, story_type=self.type)
        raise Http404(u"Invalid story type")

class StoryView(TemplateView):
    template_name="story.html"

    def get_template_names(self):
        return ['stories/%s_read.html' % self.type.slug, 'stories/read.html']

    def get_context_data(self,  **kwargs):
        if 'id' in kwargs:
            id = kwargs['id']
            quickblock = QuickBlock.objects.get(id=id)
            self.type = quickblock.quickblock_type

            return dict(story=quickblock, story_type=quickblock.quickblock_type)
        raise Http404(u"Invalid story page")
