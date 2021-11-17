from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models.base import Model


from .models import FundingProgramm, FundingSponsor, ContactMessage

# Register your models here.


class FundingProgramAdmin(ModelAdmin):
    list_filter = ('area', 'region', 'type',
                   ("type", admin.EmptyFieldListFilter),)

    readonly_fields = ('id', 'last_updated', 'who_last_updated')

    def save_model(self, request, obj, form, change) -> None:
        obj.who_last_updated = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(FundingProgramm, FundingProgramAdmin)
admin.site.register(FundingSponsor, ModelAdmin)
admin.site.register(ContactMessage, ModelAdmin)
