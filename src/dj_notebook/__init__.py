import django
import os
from django.core.management.color import no_style
from django.conf import settings as django_settings
from django_extensions.management import shells


from .shell_plus import Plus


def activate(settings: str) -> Plus:
    if settings == "test_harness":
        # Used for testing
        # NOTE: This is bad code smell, we'll improve on it
        #      when we have a better idea of what we're doing
        django_settings.configure(
            INSTALLED_APPS=[
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
                "django.contrib.staticfiles",
            ]
        )
    else:
        # Used for standard operations
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        django.setup()
    return Plus(shells.import_objects({"quiet_load": True}, no_style()))
