import django
import os
from django.core.management.color import no_style
from django.conf import settings as django_settings
from django_extensions.management import shells

from IPython.utils.capture import capture_output
from IPython.core.getipython import get_ipython

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

        # Check for Jupyter environment and display the warning if DEBUG=True
        if is_notebook() and getattr(django_settings, "DEBUG", False):
            from IPython.display import display, HTML

            warning_message = """
            <div style='background-color: #fff3cd; border-left: 
            6px solid #ffcc00; padding: 10px; margin: 10px 0;'>
            WARNING: It is strongly discouraged to run shell 
            or shell_plus in production.
            </div>
            """
            display(HTML(warning_message))

        with capture_output() as c:
            plus = Plus(shells.import_objects({"quiet_load": False}, no_style()))

        plus._import_object_history = c.stdout

        if quiet_load is False:
            plus.print()

    return plus


def is_notebook():
    """Check if we're running inside a Jupyter notebook."""
    # TODO: add logging
    try:
        ipython = get_ipython()
        if ipython is None:
            return False
        return "IPKernelApp" in ipython.config
    except Exception:
        return False
