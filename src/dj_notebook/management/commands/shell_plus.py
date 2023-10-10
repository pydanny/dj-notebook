from django_extensions.management.commands import shell_plus
from dj_notebook.utilities.dj_notebook_utils import warn_if_shell_in_production


class Command(shell_plus.Command):
    """
    Custom management command that acts as a safety wrapper over shell_plus.
    Warns users when the shell is run in a non-DEBUG environment.
    """

    def handle(self, *args, **options):
        """
        Handle the command invocation. Checks are performed before delegating to the
        original shell_plus command.
        """
        # Perform safety checks before running shell_plus
        warn_if_shell_in_production("shell_plus")

        # Delegate to the original shell_plus command
        super().handle(*args, **options)
