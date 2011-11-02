from django.db import models
from django.contrib.auth.models import User
from smartmin.models import SmartModel

class QuickBlockType(SmartModel):
    """
    Quick Block Types just group fields by a slug.. letting you do lookups by type.  In the future
    it may be nice to specify which fields should be displayed when creating fields of a new type.
    """
    name = models.CharField(max_length=75, unique=True,
                            help_text="The human readable name for this content type")
    slug = models.SlugField(max_length=50, unique=True,
                            help_text="The slug to idenfity this content type, used with the template tags")
    description = models.TextField(blank=True, null=True,
                                   help_text="A description of where this content type is used on the site and how it will be dsiplayed")

    def __unicode__(self):
        return self.name

class QuickBlock(SmartModel):
    """
    A QuickBlock is just a block of content, organized by type and priority.  All fields are optional
    letting you use them for different things.
    """
    quickblock_type = models.ForeignKey(QuickBlockType,
                                        verbose_name="Content Type",
                                        help_text="The category, or type for this content block")

    title = models.CharField(max_length=255, blank=True, null=True,
                             help_text="The title for this block of content, optional")
    content = models.TextField(blank=True, null=True,
                               help_text="The body of text for this content block, optional")
    image = models.ImageField(blank=True, null=True, upload_to='quickblocks',
                              help_text="Any image that should be displayed with this content block, optional")
    link = models.CharField(blank=True, null=True, max_length=255,
                            help_text="Any link that should be associated with this content block, optional")
    tags = models.CharField(blank=True, null=True, max_length=255,
                           help_text="Any tags for this content block, separated by spaces, can be used to do more advanced filtering, optional")
    priority = models.IntegerField(default=0,
                                   help_text="The priority for this block, higher priority blocks come first")


    def space_tags(self):
        """
        If we have tags set, then adds spaces before and after to allow for SQL querying for them.
        """
        if self.tags.strip():
            self.tags = " " + self.tags.strip().lower() + " "

    def __unicode__(self):
        return self.title
