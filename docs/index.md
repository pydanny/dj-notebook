# Home

![dj-notebook logo](img/dj-notebook-logo.png)

_Django + Jupyter notebooks made easy_

A Jupyter notebook with access to objects from the Django ORM is a powerful tool to introspect data and run ad-hoc queries.

## Features

The ever-growing list of features:

- Easy ipython notebooks with Django
- Built-in integration with the imported objects from django-extensions
- Inheritance diagrams on any object, including ORM models
- Converts any Django QuerySet to Pandas Dataframe
- Handy function for displaying mermaid charts in 
- Generates visual maps of model relations

## Examples

```python
from dj_notebook import activate
plus = activate()
plus.User.objects.all()
```

```
<QuerySet [<User: Audrey>, <User: Daniel>]>
```

!!! tip "Full Usage"

    Learn how to use all the awesome features of dj-notebook in the [usage page](/usage)!


