# config/settings/development.py
"""Local development settings. Selected by manage.py."""

from .base import *  # noqa: F403

# Local development always runs with verbose error pages, regardless of .env.
DEBUG = True

# Only this machine serves the dev site.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
