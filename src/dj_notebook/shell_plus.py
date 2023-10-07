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
from django.utils.functional import cached_property

import IPython
from IPython.display import display
import pandas as pd

from django.db import models as django_models
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

    @cached_property
    def graph_data(self) -> dict:
        """Cached property for the graph data."""
        return graph_model_data(self.helpers)

    def graph_model(self, model: django_models.Model, max_nodes: int = 20) -> None:
        """Draw a diagram of the specified model in the database."""
        if len(self.graph_data[model]) > max_nodes:
            console.print(
                f"[red bold]Warning: Model {model} has more than {max_nodes} nodes. "
                "The diagram may be too large to render."
            )

        output = """flowchart TD\n"""
        for edge in self.graph_data[model]:
            output += f"  {edge['from']} --- {edge['to']}\n"
        display_mermaid(output)


def make_edge(a: django_models.Model, b: django_models.Model) -> dict:
    # if a == b:
    #     raise ValueError("Cannot create an edge between the same model.")
    nodes = sorted([a._meta.model_name, b._meta.model_name])
    return {"from": nodes[0], "to": nodes[1], "str": f"{nodes[0]} --- {nodes[1]}"}


def graph_model_data(helpers: dict):
    """Edges allow us to build a graph of the models in the database."""
    data = {}

    # Do first loop to get relations in one direction
    for model_name, model in helpers.items():
        if getattr(model, "_meta", None) is None:
            continue

        relations = [
            field
            for field in model._meta.get_fields(include_hidden=True)
            if isinstance(field, django_models.ForeignObjectRel)
        ]

        # Set defaults
        data.setdefault(model, [])
        for relation in relations:
            # Set defaults
            data.setdefault(relation.related_model, [])

            # Add the edge            
            data[model].append(make_edge(a=model, b=relation.related_model))
            data[relation.related_model].append(
                make_edge(a=model, b=relation.related_model)
            )

    return data
