import ast
import os
from pathlib import Path
from typing import Generator, Tuple

from dotenv import load_dotenv


# taken from dotenv, which declares a similar type (but it doesn't look public...)
# review note: the | syntax is new in python 3.10. If older pythons are generally being supported here, this should be
# rewritten as Union[str, os.PathLike[str]]
StrPath = str | os.PathLike[str]


def setdefault_calls(module_path: Path) -> Generator[ast.Call, None, None]:
    """Yields all calls to `os.environ.setdefault` within a module."""
    with open(module_path, "r") as module_src:
        parsed_module = ast.parse(module_src.read())
    environ_id = None
    for node in ast.walk(parsed_module):
        if isinstance(node, ast.ImportFrom) and node.module == "os":
            for name in node.names:
                if isinstance(name, ast.alias) and name.name == "environ":
                    environ_id = name.asname if name.asname is not None else name.name
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "setdefault"
        ):
            if (
                isinstance(node.func.value, ast.Attribute)
                and node.func.value.attr == "environ"
            ):
                if (
                    isinstance(node.func.value.value, ast.Name)
                    and node.func.value.value.id == "os"
                ):
                    yield node
            elif (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == environ_id
            ):
                yield node


def is_root(path: Path) -> bool:
    """
    returns True if the supplied path is the root directory. This is only here because it seems clearer than
    `path.samefile(path.parent)` when reading a loop that walks up a directory hierarchy.
    """
    return path.samefile(path.parent)


# review note: the | syntax is new in python 3.10. If older pythons are generally being supported here, the type for
# dotenv_file should be rewritten as Optional[StrPath] = None and the return type should be annotated as
# Tuple[str, Optional[str]]
def find_django_settings_module(
    *, dotenv_file: StrPath | None = None
) -> Tuple[str, str | None]:
    """
    Find the name of the first settings module from the environment or the closest `manage.py` file.
    Returns: a tuple(source, module name) telling the caller where the module was found and the name of the module.

    The optional, keyword-only argument `dotenv_file` will be explicitly loaded prior to searching the environment,
    if supplied.
    """
    # First see if this has either already been set in the environment or put in a .env file that python-dotenv will
    # treat that way
    settings_module = None
    if not dotenv_file:
        source = "environment"
        settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", None)
    if not settings_module:
        # load with override=True if the caller has specified a dotenv file explicitly
        source = "dotenv"
        load_dotenv(dotenv_file, override=bool(dotenv_file))
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", None)
    # If we get nothing from the environment, look for a `manage.py` script containing a call that sets a default in the
    # current working directory or in any parent. This should accommodate the common pattern of
    # - app1
    # - app2
    # - project
    # --> settings.py
    # - scripts
    # - notebooks
    # --> analysis_notebook.ipynb
    # - manage.py
    search_dir = Path.cwd().resolve()
    while settings_module is None:
        manage_py = search_dir / "manage.py"
        if manage_py.is_file():
            for call in setdefault_calls(manage_py):
                if (
                    len(call.args) == 2
                    and call.args[0].value == "DJANGO_SETTINGS_MODULE"
                ):
                    settings_module = call.args[1].value
                    source = f"{manage_py.resolve().absolute()}"
        elif is_root(search_dir):
            break
        else:
            search_dir = search_dir.parent.resolve()
    if not settings_module:
        # Finally, go one level down into children of the current working directory to see if a `manage.py` with a default
        # for `DJANGO_SETTINGS_MODULE` can be found there. This accommodates the common pattern of
        # - analysis.ipynb
        # - src
        # --> manage.py
        # --> project
        # ----> settings.py
        # ...
        for p in [Path(subdir) for subdir in os.scandir(Path.cwd())]:
            manage_py = p / "manage.py"
            if manage_py.is_file():
                for call in setdefault_calls(manage_py):
                    if (
                        len(call.args) == 2
                        and call.args[0].value == "DJANGO_SETTINGS_MODULE"
                    ):
                        settings_module = call.args[1].value
                        source = manage_py.resolve().absolute()
                        break

    return str(source), settings_module
