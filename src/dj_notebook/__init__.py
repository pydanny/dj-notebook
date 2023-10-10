import os

import django
from django.conf import settings as django_settings
from django.core.management.color import no_style
from django_extensions.management import shells
from IPython.utils.capture import capture_output
from rich.status import Status

from .shell_plus import Plus


def activate(settings: str, quiet_load: bool = True) -> Plus:
    with Status(
        "Loading dj-notebook...\n  Use Plus.print() to see what's been loaded.",
        spinner="bouncingBar",
    ):
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

        with capture_output() as c:
            plus = Plus(shells.import_objects({"quiet_load": False}, no_style()))

        plus._import_object_history = c.stdout

        if quiet_load is False:
            plus.print()

    return plus
