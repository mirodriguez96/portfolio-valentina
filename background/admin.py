from django.contrib import admin

# Register your models here.
from .models import Background


class BackgroundAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Background, BackgroundAdmin)
