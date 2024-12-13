from .backends import DjangoResultBackend

__version__ = "0.1.1"

default_app_config = (
    "django_dramatiq_result_backend.apps.DjangoDramatiqResultBackendConfig"
)

__all__ = ["DjangoResultBackend"]
