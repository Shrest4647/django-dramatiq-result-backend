from django.db import models
from datetime import datetime


class Result(models.Model):
    """A model to store task results.

    Attributes:
        message_key (str): The message key of the task.
        result_data (dict): The result data of the task.
        expiration_time (datetime): The expiration time of the result.
        is_expired (bool): Whether the result has expired.
    """

    message_key = models.CharField(max_length=255, unique=True)
    result_data = models.JSONField(null=True, blank=True)
    expiration_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self) -> bool:
        return datetime.now() > self.expiration_time
