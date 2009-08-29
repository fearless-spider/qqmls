from django.contrib import admin
from qqmls.news.models import Entry


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
