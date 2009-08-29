from django.contrib import admin
from qqmls.events.models import Event, Agenda


class EventAdmin(admin.ModelAdmin):
    pass


class AgendaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Agenda, AgendaAdmin)
