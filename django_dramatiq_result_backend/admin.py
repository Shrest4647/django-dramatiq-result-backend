from django.contrib import admin

from .models import Result


# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """Admin for the Result model."""

    list_display = (
        "__str__",
        "message_key",
        "result_data",
        "created_at",
        "expiration_time",
    )
    readonly_fields = ("message_key", "created_at", "expiration_time")
    search_fields = ("message_key",)
