# Django Dramatiq Result Backend

A Django-based ResultBackend for [Dramatiq](https://dramatiq.io/).

## Features

- Store and retrieve task results using Django's ORM.
- Automatically handle result expiration.

## Installation

```bash
pip install django-dramatiq-result-backend
```

## Usage

### Configure Django

Add `django_dramatiq_result_backend` to your `INSTALLED_APPS` in `settings.py`.

### Configure Dramatiq Result Backend

```python
# settings.py

DRAMATIQ_RESULT_BACKEND = {
    "BACKEND": "django_dramatiq_result_backend.backends.DjangoDramatiqResultBackend",
    "OPTIONS": {
        "model": "django_dramatiq_result_backend.Result",
        "expiration": 30 * 60 * 60 * 24,  # 30 days
    },
}

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

