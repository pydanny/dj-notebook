import sys
import warnings
from django.conf import settings

try:
    from termcolor import colored
except ImportError:

    def colored(text, color=None, on_color=None, attrs=None):
        """Fallback function if termcolor is not available."""
        return text


def warn_if_shell_in_production(command_name):
    """
    Check if Django is running in DEBUG mode and raise warnings
    if shell or shell-plus invoked.

    Args:
        command_name (str): Name of the command to check
    """
    if settings.DEBUG and command_name in ["shell", "shell_plus"]:
        warning_message = (
            f"WARNING: It is strongly discouraged to run "
            f"'{command_name}' in production."
        )

        # Display the warning in JupyterLab Notebook
        warnings.warn(warning_message, stacklevel=2)

        # Print a red warning message to the shell
        print(colored(warning_message, "red"), file=sys.stderr)
