from django.contrib import admin
from financial.models import (Account, GLAccountCategories)
from django.core.exceptions import ValidationError

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
        except ValidationError as e:
            form.add_error(None, e)
            return
        super().save_model(request, obj, form, change)

admin.site.register(Account, AccountAdmin)
admin.site.register(GLAccountCategories)