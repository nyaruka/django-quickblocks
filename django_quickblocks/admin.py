from django.contrib import admin
from reversion.admin import VersionAdmin
from models import QuickBlock, QuickBlockType


class QuickBlockTypeAdmin(VersionAdmin):
    list_display = ('slug', 'created_on', 'created_by')
    ordering = ('-created_on',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(QuickBlockType, QuickBlockTypeAdmin)

class QuickBlockAdmin(VersionAdmin):
    list_display = ('title', 'quickblock_type', 'is_active', 'priority', 'created_on', 'created_by')
    list_filter = ('is_active', 'quickblock_type')
    ordering = ('-is_active', 'quickblock_type', '-priority')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(QuickBlock, QuickBlockAdmin)

