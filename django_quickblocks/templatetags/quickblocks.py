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
from django_quickblocks.models import QuickBlockType, QuickBlock

register = template.Library()


@register.simple_tag(takes_context=True)
def load_quickblocks(context, slug, tag=None):
    try:
        quickblock_type = QuickBlockType.objects.get(slug=slug)
    except QuickBlockType.DoesNotExist:
        return getattr(settings, 'QUICKBLOCK_STRING_IF_INVALID', '<b><font color="red">QuickBlockType with slug: %s not found</font></b>') % slug
 
    quickblocks = QuickBlock.objects.filter(quickblock_type=quickblock_type, is_active=True).order_by('-priority')

    # filter by our tag if one was specified
    if not tag is None:
        quickblocks = quickblocks.filter(tags__icontains=tag)

    context[slug] = quickblocks
    return ''

@register.simple_tag(takes_context=True)
def load_qbs(context, slug, tag=None):
    return load_quickblocks(context, slug, tag)


