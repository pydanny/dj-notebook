# Activation

We try our best to make activating dj-notebook as easy as possible. It should be easy to do, but more complicated projects will require manipulation of paths. The goal of this page is to provide all the instruction users may need or link to external docs as necessary.

!!! info "Using dj-notebook with PyCharm"

    If using PyCharm the [instructions described here](../pycharm) are a very useful reference.

## Auto-discovery

_New in dj-notebook 0.6.0_

Create an ipython notebook in the same directory as `manage.py`. In VSCode,
simply add a new `.ipynb` file. If using Jupyter Lab, use the `File -> New ->
Notebook` menu option. 

In the first cell type the following:

```python

from dj_notebook import activate

plus = activate()
```

## Specifying settings

If that doesn't work, find the project's `manage.py` file and open it.
Copy whatever is being set to `DJANGO_SETTINGS_MODULE` as a string
argument to `activate` function like so:

```python
plus = activate('book_store.settings')
```
 
## Using `.env` file to specify settings

_New in dj-notebook 0.6.0_

dj-notebook has support for .env files. Assuming our `.env` file is at `/me/projects/djangopackages/.env` and looks like this:

```
SECRET_KEY=TopSecretValueHere
DEBUG=True
DJANGO_SETTINGS_MODULE=book_store.settings
```

Then we can pass in that file in this manner:

```python
plus = activate(dotenv_file='/me/projects/djangopackages/.env')
```

## Advanced: Modifying the Path

This advanced technique is when you want to activate dj-notebook in a different directory from the Django project. For example, in dj-notebook the [usage](./usage) page is completely seperate:

```
docs
└── usage.ipynb
tests/django_test_project
└── manage.py
```

To address that, in the `docs/usage.ipynb` file we modify the path to include `django_test_project` so dj-notebook can find with a simple `activate()` call:

```python
import pathlib
import sys

here = pathlib.Path(".").parent
PROJECT_ROOT = (here / ".." / "tests" / "django_test_project").resolve()
sys.path.insert(0, str(PROJECT_ROOT))
```

!!! note

    For the sake of clarity, the above code is not visible in dj-notebook's rendered [usage](./usage) instructions. This is a hidden cell, so look in the [unrendered usage.ipynb file](https://github.com/pydanny/dj-notebook/blob/main/docs/usage.ipynb).