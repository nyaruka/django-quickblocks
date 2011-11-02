from .models import *
from smartmin.views import *
from django import forms

class QuickBlockCRUDL(SmartCRUDL):
    model = QuickBlock
    permissions = True
    actions = ('create', 'update', 'list')

    class Update(SmartUpdateView):
        def pre_save(self, obj):
            obj = super(QuickBlockCRUDL.Update, self).pre_save(obj)
            obj.space_tags()
            return obj

    class Create(SmartCreateView):
        grant_permissions = ('django_quickblocks.change_quickblock',)

        def pre_save(self, obj):
            obj = super(QuickBlockCRUDL.Create, self).pre_save(obj)
            obj.space_tags()
            return obj
            
    class List(SmartListView):
        fields = ('title', 'priority', 'quickblock_type', 'tags')
        link_fields = ('title',)

class QuickBlockTypeCRUDL(SmartCRUDL):
    model = QuickBlockType
    permissions = True
    actions = ('create', 'update', 'list')

    class List(SmartListView):
        fields = ('name', 'slug')
        link_fields = ('name',)
