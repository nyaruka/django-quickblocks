from django.contrib import admin
from reversion.admin import VersionAdmin
from models import QuickBlock, QuickBlockType


class QuickBlockTypeAdmin(VersionAdmin):
    list_display = ('slug', 'created', 'owner')
    ordering = ('-created',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

admin.site.register(QuickBlockType, QuickBlockTypeAdmin)

class QuickBlockAdmin(VersionAdmin):
    list_display = ('title', 'type', 'active', 'priority', 'created', 'owner')
    list_filter = ('active', 'type')
    ordering = ('-active', 'type', '-priority')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

admin.site.register(QuickBlock, QuickBlockAdmin)

