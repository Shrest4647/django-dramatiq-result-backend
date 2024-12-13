from django.contrib import admin

from .models import Result


# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """Admin for the Result model."""

    fields = (
        "id",
        "message_key",
        "result_data",
        "created_at",
        "expiration_time",
        "is_expired",
    )
    list_display = ("id", "message_key", "created_at", "expiration_time", "is_expired")
    search_fields = ("message_key",)
