import importlib
import os
import sys
import warnings
from pathlib import Path

import django
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.color import no_style
from django_extensions.management import shells
from IPython.utils.capture import capture_output
from rich.status import Status

from .config_helper import StrPath, find_django_settings_module
from .shell_plus import Plus


__version__ = "0.6.1"


def activate(
    settings: str = None,
    quiet_load: bool = True,
    *,
    dotenv_file: StrPath | None = None,
    search_dir: StrPath | None = None,
) -> Plus:
    with Status(
        "Loading dj-notebook...\n  Use Plus.print() to see what's been loaded.",
        spinner="bouncingBar",
    ):
        if settings:
            # If the caller specified a settings module explicitly, use that
            os.environ["DJANGO_SETTINGS_MODULE"] = settings
        else:
            source, discovered_settings = find_django_settings_module(
                dotenv_file=dotenv_file,
                search_dir=search_dir,
            )
            if discovered_settings:
                if not quiet_load:
                    print(
                        f"Using {discovered_settings} as DJANGO_SETTINGS_MODULE, discovered from {source}"
                    )
                os.environ["DJANGO_SETTINGS_MODULE"] = discovered_settings
                try:
                    _ = importlib.util.find_spec(discovered_settings)
                except ModuleNotFoundError:
                    source_path = Path(source)
                    if source.endswith("manage.py") and source_path.is_file():
                        source_dir = Path(source).parent.absolute()
                        warnings.warn(
                            f"{discovered_settings} from {source} could not be loaded. Adding {str(source_dir)} to search path."
                        )
                        sys.path.append(str(source_dir))
            else:
                raise ImproperlyConfigured(
                    "DJANGO_SETTINGS_MODULE was not specified and could not be discovered."
                )
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        try:
            django.setup()
        except ModuleNotFoundError as e:
            raise ImproperlyConfigured(
                f"DJANGO_SETTINGS_MODULE {e.name} could not be loaded in django.setup()"
            )

        with capture_output() as c:
            plus = Plus(shells.import_objects({"quiet_load": False}, no_style()))

        plus._import_object_history = c.stdout

        # Log a warning message when DEBUG is set to False
        if not plus.settings.DEBUG:
            warnings.warn("Django is running in production mode with dj-notebook.")

        if quiet_load is False:
            plus.print()

    return plus
