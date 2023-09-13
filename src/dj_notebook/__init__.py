"""
This module is intended to be imported at the beginning of a jupyter notebook
to enable access to django objects with everything from django-extensions'
shell_plus command preloaded in the namespace:

    import dj_notebook as djnb

As it accesses the database, it requires that:
- The database is running in the background
- The database connection variables are correctly configured
"""


import base64
import os
import sys

import IPython
import django
from django.core.management.color import no_style
from django_extensions.management import shells
from IPython.display import display
import dotenv

dotenv.load_dotenv('.dj-notebook')

# TODO provide sensible default for PROJECT_PATH
# TODO save PROJECT_PATH and DJANGO_SETTINGS_MODULE
# PROJECT_PATH = input("/Users/drg/projects/dj_notebook/tests/django_test_project")
# if not PROJECT_PATH:
#     PROJECT_PATH = "/Users/drg/projects/dj_notebook/tests/django_test_project"
PROJECT_PATH = os.getenv('PROJECT_PATH')
sys.path.insert(0, PROJECT_PATH)
# for p in sys.path:
#     print(p)

# TODO provide sensible default for DJANGO_SETTINGS_MODULE
# DJANGO_SETTINGS_MODULE = input("book_store.settings")
# if not DJANGO_SETTINGS_MODULE:
#     DJANGO_SETTINGS_MODULE = "book_store.settings"
# print("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# for k,v in os.environ.items():
#     print(k, v)

django.setup()
print("Django loaded")


class DiagramClass:
    """This class draws a class diagram for a given class and its ancestors."""

    def __init__(self, base_class: type) -> None:
        self.base_class = base_class

        # To avoid duplicates the graph is a set
        self.graph = set()

        # Add the base_class to the graph
        self.graph.add(
            f'  class {self.namify(self.base_class)}["{self.base_class.__module__}::{self.base_class.__name__}"]'  # noqa: E501
        )

        # Draw connections between the base_class and its ancestors
        self.draw_connections(self.base_class)

        # Use Mermaid to render the graph and Ipthon to display it
        self.display_graph()

    def draw_connections(self, class_: type) -> None:
        """Draw connections between a class and its ancestors,
        includes nodes and edges."""
        for base in class_.__bases__:
            if base is not object:
                base_name = self.namify(base)
                self.graph.add(
                    f'  class {base_name}["{base.__module__}::{base.__name__}"]'
                )
                connection = f"  {base_name} <|-- {self.namify(class_)}"
                self.graph.add(connection)
                self.draw_connections(base)

    def namify(self, class_: object) -> str:
        """This provides a node name that keeps Mermaid happy."""
        return f"{class_.__module__}_{class_.__name__}".replace(".", "_")

    def display_graph(self) -> None:
        # Convert the set to a \n-seperated text file prefixed
        # with the classDiagram keyword from mermaidjs
        text = "classDiagram\n" + "\n".join(self.graph)

        # Prepare the graph for display
        graphbytes = text.encode("ascii")
        base64_bytes = base64.b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")
        # Use Mermaid to render the graph and Ipthon to display it
        display(IPython.display.Image(url="https://mermaid.ink/img/" + base64_string))


class Plus:
    """Location of all the objects loaded by shell_plus and extra
    Jupyter-specific utilities."""

    def __init__(self, helpers: dict[str, object]) -> None:
        self.helpers = helpers

    def __getattribute__(self, name: str) -> object:
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            helpers = object.__getattribute__(self, "helpers")
            if name in helpers:
                return helpers[name]
            else:
                raise

    def diagram(self, class_: object) -> None:
        """Draw a class diagram for a given class and its ancestors."""
        if not isinstance(class_, type):
            class_ = type(class_)
        DiagramClass(class_)

        # DiagramClass(class_)

    def print(self) -> None:
        """Print all the objects contained by the Plus object."""
        for k, v in self.__dict__.items():
            print(k, v)  # noqa: K104


# load django-extensions shell_plus
djnb: Plus = Plus(shells.import_objects({"quiet_load": True}, no_style()))
