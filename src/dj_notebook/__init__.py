import django
import os
from django.core.management.color import no_style
from django_extensions.management import shells

from .shell_plus import Plus


def activate(settings: str) -> Plus:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()
    return Plus(shells.import_objects({"quiet_load": True}, no_style()))
