import os
import warnings

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
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        django.setup()

        with capture_output() as c:
            plus = Plus(shells.import_objects({"quiet_load": False}, no_style()))

        plus._import_object_history = c.stdout

        # Log a warning message when DEBUG is set to False
        if not plus.settings.DEBUG:
            warnings.warn("Django is running in production mode with dj-notebook.")

        if quiet_load is False:
            plus.print()

    return plus
