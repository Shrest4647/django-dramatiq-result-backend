from datetime import datetime, timedelta
from dramatiq.results.backend import ResultBackend, Missing
import typing
from django_dramatiq_result_backend.models import Result


class DjangoResultBackend(ResultBackend):
    """A Django-based ResultBackend for Dramatiq."""

    def _get(self, message_key: str):
        """Get a result from the backend.

        Args:
            message_key (str): The message key of the task.

        Returns:
            typing.Any: The result data if found, Missing otherwise.
        """

        try:
            result = Result.objects.get(message_key=message_key)

            # Check if the result has expired.
            if result.is_expired:
                # Delete the expired result and return Missing.
                result.delete()
                return Missing

            return result.result_data
        except Result.DoesNotExist:
            return Missing

    def _store(self, message_key: str, result: typing.Any, ttl: int):
        """Store a result in the backend.

        Args:
            message_key (str): The message key of the task.
            result (typing.Any): The result data to store.
            ttl (int): The time-to-live (TTL) of the result.
        """
        expiration_time = datetime.now() + timedelta(seconds=ttl)

        Result.objects.update_or_create(
            message_key=message_key,  # Use the message key as the unique identifier.
            defaults={
                "result_data": result,  # Store the serialized result data.
                "expiration_time": expiration_time,  # Set the expiration time.
            },
        )
