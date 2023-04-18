from django.contrib import admin
from Vtuber.models import Vtuber


# Register your models here.
@admin.register(Vtuber)
class VtubeAdmin(admin.ModelAdmin):
    list_display = ['name', 'Ddate', 'tag_list']

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
