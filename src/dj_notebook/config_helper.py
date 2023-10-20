import ast
import os
from pathlib import Path
from typing import Generator, Tuple

from dotenv import load_dotenv


def setdefault_calls(module_path: Path) -> Generator[ast.Call, None, None]:
    """ Yields all calls to `os.environ.setdefault` within a module. """
    with open(module_path, "r") as module_src:
        parsed_module = ast.parse(module_src.read())
    environ_id = "environ"
    for node in ast.walk(parsed_module):
        if isinstance(node, ast.ImportFrom) and node.module == "os":
            for name in node.names:
                if isinstance(name, ast.alias):
                    if name.name == "environ" and name.asname is not None:
                        environ_id = name.asname
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "setdefault":
            if isinstance(node.func.value, ast.Attribute) and node.func.value.attr == "environ":
                if isinstance(node.func.value.value, ast.Name) and node.func.value.value.id == "os":
                    yield node
            elif isinstance(node.func.value, ast.Name) and node.func.value.id == environ_id:
                yield node


def is_root(path: Path) -> bool:
    """

    Args:
        path: directory to test

    Returns:
        True if the path is the same as the parent directory and therefore the root of the directory tree being searched

    """
    return path.samefile(path.parent)


def find_django_settings_module() -> Tuple[str | None, str | None]:
    """

    Returns:
        A sane default value from the environment or from a `manage.py` script for the django project's settings module,
        or None if one can't be inferred

    """
    # First see if this has either already been set in the environment or put in a .env file that python-dotenv will
    # treat that way
    source = "environment"
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", None)
    if not settings_module:
        source = "dotenv"
        load_dotenv()
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
                if len(call.args) == 2 and call.args[0].value == "DJANGO_SETTINGS_MODULE":
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
                    if len(call.args) == 2 and call.args[0].value == "DJANGO_SETTINGS_MODULE":
                        settings_module = call.args[1].value
                        source = manage_py.resolve().absolute()
                        break

    return str(source), settings_module

