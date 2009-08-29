from django.contrib import admin
from qqmls.accounts.models import Person, Address


class PersonAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
