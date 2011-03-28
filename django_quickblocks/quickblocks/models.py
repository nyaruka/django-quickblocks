from django.db import models
from django.contrib.auth.models import User


class QuickBlockType(models.Model):
    """
    Quick Block Types just group fields by a slug.. letting you do lookups by type.  In the future
    it may be nice to specify which fields should be displayed when creating fields of a new type.
    """
    
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.slug

class QuickBlock(models.Model):
    """
    A QuickBlock is just a block of content, organized by type and priority.  All fields are optional
    letting you use them for different things.
    """

    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='quickblocks')
    link = models.CharField(blank=True, null=True, max_length=255)
    priority = models.IntegerField(default=0)
    type = models.ForeignKey(QuickBlockType)
    owner = models.ForeignKey(User, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
