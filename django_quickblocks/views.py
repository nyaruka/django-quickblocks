from .models import *
from smartmin.views import *
from django import forms

class QuickBlockCRUDL(SmartCRUDL):
    model = QuickBlock
    permissions = True
    actions = ('create', 'update', 'list')

    class Update(SmartUpdateView):
        fields = ('title', 'summary', 'content', 'image', 'color', 'link', 'video_id', 'quickblock_type', 'priority', 'is_active')

        def pre_save(self, obj):
            obj = super(QuickBlockCRUDL.Update, self).pre_save(obj)
            obj.space_tags()
            return obj

        def derive_exclude(self):
            exclude = super(QuickBlockCRUDL.Update, self).derive_exclude()

            block_type = self.object.quickblock_type

            if not block_type.has_summary:
                exclude.append('summary')

            if not block_type.has_video:
                exclude.append('video_id')

            if not block_type.has_title:
                exclude.append('title')

            if not block_type.has_tags:
                exclude.append('tags')

            if not block_type.has_image:
                exclude.append('image')

            if not block_type.has_link:
                exclude.append('link')

            if not block_type.has_color:
                exclude.append('color')

            return exclude

        def get_context_data(self, *args, **kwargs):
            context = super(QuickBlockCRUDL.Update, self).get_context_data(*args, **kwargs)
            context['type'] = self.object.quickblock_type
            return context

        def derive_title(self):
            return "Edit %s" % self.object.quickblock_type.name

    class Create(SmartCreateView):
        grant_permissions = ('django_quickblocks.change_quickblock',)

        def derive_exclude(self):
            exclude = super(QuickBlockCRUDL.Create, self).derive_exclude()

            block_type = self.get_type()
            if block_type:
                exclude.append('quickblock_type')

                if not block_type.has_summary:
                    exclude.append('summary')

                if not block_type.has_video:
                    exclude.append('video_id')

                if not block_type.has_title:
                    exclude.append('title')

                if not block_type.has_tags:
                    exclude.append('tags')

                if not block_type.has_image:
                    exclude.append('image')

                if not block_type.has_link:
                    exclude.append('link')

                if not block_type.has_color:
                    exclude.append('color')

            return exclude

        def derive_initial(self, *args, **kwargs):
            initial = super(QuickBlockCRUDL.Create, self).derive_initial(*args, **kwargs)
            quickblock_type = self.get_type()
            other_blocks = QuickBlock.objects.filter(is_active=True, quickblock_type=quickblock_type).order_by('-priority')
            if not other_blocks:
                initial['priority'] = 0
            else:
                initial['priority'] = other_blocks[0].priority + 1
            return initial

        def derive_title(self):
            block_type = self.get_type()
            if block_type:
                return "Create %s" % block_type.name
            else:
                return "Create Content Block"

        def get_type(self):
            if 'type' in self.request.REQUEST:
                return QuickBlockType.objects.get(id=self.request.REQUEST.get('type'))
            return None

        def get_context_data(self, *args, **kwargs):
            context = super(QuickBlockCRUDL.Create, self).get_context_data(*args, **kwargs)
            context['type'] = self.get_type()
            return context

        def pre_save(self, obj):
            obj = super(QuickBlockCRUDL.Create, self).pre_save(obj)

            block_type = self.get_type()
            if block_type:
                obj.quickblock_type = block_type
            
            obj.space_tags()
            return obj
            
    class List(SmartListView):
        fields = ('title', 'priority', 'quickblock_type', 'tags')
        link_fields = ('title',)
        default_order = '-modified_on'
        search_fields = ('title__icontains', 'content__icontains', 'summary__icontains')
        title = "Content Blocks"

        def get_type(self):
            if 'type' in self.request.REQUEST:
                return QuickBlockType.objects.get(id=self.request.REQUEST.get('type'))
            elif 'slug' in self.request.REQUEST:
                return QuickBlockType.objects.get(slug=self.request.REQUEST.get('slug'))
            return None

        def get_queryset(self, **kwargs):
            queryset = super(QuickBlockCRUDL.List, self).get_queryset(**kwargs)

            quickblock_type = self.get_type()
            if quickblock_type:
                queryset = queryset.filter(quickblock_type=quickblock_type)

            queryset = queryset.filter(quickblock_type__is_active=True)
                
            return queryset

        def get_context_data(self, *args, **kwargs):
            context = super(QuickBlockCRUDL.List, self).get_context_data(*args, **kwargs)
            context['types'] = QuickBlockType.objects.filter(is_active=True)
            context['filtered_type'] = self.get_type()
            return context

class QuickBlockTypeCRUDL(SmartCRUDL):
    model = QuickBlockType
    actions = ('create', 'update', 'list')

    class List(SmartListView):
        title = "Content Types"
        fields = ('name', 'slug', 'description')
        link_fields = ('name',)

class QuickBlockImageCRUDL(SmartCRUDL):
    model = QuickBlockImage
    actions = ('create', 'update', 'list')

    class Update(SmartUpdateView):
        exclude = ('quickblock', 'modified_by', 'modified_on', 'created_on', 'created_by', 'width', 'height')
        title = "Edit Image"
        success_message = "Image edited successfully."        

        def get_success_url(self):
            return reverse('django_quickblocks.quickblock_update', args=[self.object.quickblock.id])

    class Create(SmartCreateView):
        exclude = ('quickblock', 'is_active', 'modified_by', 'modified_on', 'created_on', 'created_by', 'width', 'height')
        title = "Add Image"
        success_message = "Image added successfully."

        def derive_initial(self, *args, **kwargs):
            initial = super(QuickBlockImageCRUDL.Create, self).derive_initial(*args, **kwargs)
            quickblock = QuickBlock.objects.get(pk=self.request.REQUEST.get('quickblock'))
            images = quickblock.sorted_images()
            if not images:
                initial['priority'] = 0
            else:
                initial['priority'] = images[0].priority + 1
            return initial

        def get_success_url(self):
            return reverse('django_quickblocks.quickblock_update', args=[self.object.quickblock.id])

        def pre_save(self, obj):
            obj = super(QuickBlockImageCRUDL.Create, self).pre_save(obj)
            obj.quickblock = QuickBlock.objects.get(pk=self.request.REQUEST.get('quickblock'))
            return obj

        

