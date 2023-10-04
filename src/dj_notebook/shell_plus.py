"""
This module is intended to be imported at the beginning of a jupyter notebook
to enable access to django objects with everything from django-extensions'
shell_plus command and other utilities.:

    from dj_notebook import activate
    plus = activate

As it accesses the database, it requires that:
- The database is running in the background
- The database connection variables are correctly configured
"""


import base64

import IPython
from IPython.display import display
import pandas as pd

from django.db.models.query import QuerySet
from django_pandas.io import read_frame

from rich.console import Console
from rich.syntax import Syntax

console = Console()


def display_mermaid(graph: str) -> None:
    """Renders the display with Mermaid."""
    graphbytes = graph.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    display(IPython.display.Image(url="https://mermaid.ink/img/" + base64_string))


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

        # Convert the set to a \n-seperated text file prefixed
        # with the classDiagram keyword from mermaidjs
        text = "classDiagram\n" + "\n".join(self.graph)

        # Use Mermaid to render the graph and Ipthon to display it
        display_mermaid(text)

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

    def print(self) -> None:
        """Print all the objects contained by the Plus object."""
        console.print(Syntax(self._import_object_history, "python"))

    def read_frame(self, qs: QuerySet) -> pd.DataFrame:
        """Converts a Django QuerySet into a Pandas DataFrame."""
        return read_frame(qs)

    def mermaid(self, diagram: str) -> None:
        """Render a mermaid diagram."""
        display_mermaid(diagram)
