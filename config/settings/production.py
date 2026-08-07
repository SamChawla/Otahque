# config/settings/production.py
"""Production settings. Selected by config/wsgi.py and config/asgi.py."""

from decouple import Csv, config

from .base import *  # noqa: F403

# Detailed error pages must never reach real users.
DEBUG = False

# Real hostnames come from the environment, never hardcoded. Required.
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Security hardening. Full treatment arrives in Chapter 42; these are the
# essentials so a production deploy is safe from day one.
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
