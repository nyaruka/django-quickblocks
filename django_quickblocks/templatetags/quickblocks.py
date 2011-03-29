"""
This module offers one templatetag called ``load_quickblocks``.

``load_quickblocks`` does a query for all active QuickBlock objects
for the passed in QuickBlockType. (identified by the slug)  You can
then access that list within your context.

It accepts 1 parameter:

    slug
        The slug/key of the QuickBlockType to load QuickBlocks for.

        If you want to pass it by name, you have to use quotes on it.
        Otherwise just use the variable name.

Syntax::

    {% load_quickblocks [name] %}

Example usage::

    {% load quickblocks %}

    ...

    {% load_quickblocks "home_banner_blocks" %}

    ...

    Note: You may also use the shortcut tag 'load_qbs' eg: {% load_qbs "home_banner_blocks %}

.. note::

    If you specify a slug that has no associated quick block, then an error message
    will be inserted in your template.  You may change this text by setting
    the value of the QUICKBLOCK_STRING_IF_INVALID setting.

"""

from django import template
from django.conf import settings
from django.db import models


register = template.Library()

QuickBlockType = models.get_model('django_quickblocks', 'quickblocktype')
QuickBlock = models.get_model('django_quickblocks', 'quickblock')

class LoadQuickBlocksNode(template.Node):
    def __init__(self, slug, is_variable):
       self.slug = slug
       self.is_variable = is_variable

    def render(self, context):
        real_slug = self.slug

        try:
            quickblock_type = QuickBlockType.objects.get(slug=real_slug)
        except QuickBlockType.DoesNotExist:
            return getattr(settings, 'QUICKBLOCK_STRING_IF_INVALID', '<b><font color="red">QuickBlockType with slug: "%s" not found.</font></b>' % real_slug)


        quickblocks = QuickBlock.objects.filter(type=quickblock_type.pk, active=True).order_by('-priority')
        context[real_slug] = quickblocks

        return ''

def do_load_quickblocks(parser, token):
        tokens = token.split_contents()
        is_variable = False
        slug = None

        if len(tokens) != 2:
            raise template.TemplateSyntaxError, \
                "%r tag should have 2 arguments" % (tokens[0],)
        tag_name, slug = tokens

        # Check to see if the slug is properly double/single quoted
        if not (slug[0] == slug[-1] and slug[0] in ('"', "'")):
            is_variable = True
            slug = slug
        else:
            slug = slug[1:-1]

        return LoadQuickBlocksNode(slug, is_variable)

register.tag('load_quickblocks', do_load_quickblocks)
register.tag('load_qbs', do_load_quickblocks)
