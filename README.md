# dj-notebook

A Jupyter notebook with access to objects from the Django ORM is a powerful tool to introspect data and run ad-hoc queries.

## Features

- Easy ipython notebooks with Django
- Built-in integration with the imported objects from django-extensions
- Inheritance diagrams on any object, including ORM models

## Installation

Use your installation tool of choice, here we use venv and pip:

```bash
python -m venv venv
source venv/bin/activate
pip install dj_notebook
```

## Usage

First, find your project's `manage.py` file and open it. Copy whatever is being set to `DJANGO_SETTINGS_MODULE` into your clipboard.

Create an ipython notebook in the same directory as `manage.py`. Then in the first cell enter:

```python
from dj_notebook import activate

plus = activate("DJANGO_SETTINGS_MODULE_VALUE")
```

In future cells, you can now load and run Django objects, including the ORM. This three line snippet should give an idea of what you can now do:

```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all()
```

## Usage Plus

But wait, it gets better!

When you activated the Django environment, you instantiated a variable called 'plus'. The 'plus' variable  is an object that contains everything loaded from django-extensions' `shell_plus`. Here's a demonstration, try running this snippet:

```python
plus.User.objects.all()
```

We also provide a utility for introspection of classes, which can be useful in sophisticated project architectures. Running this code in a Jupyter notebook shell:

```python
plus.diagram(plus.User)
```

Generates this image

<img src="https://mermaid.ink/img/Y2xhc3NEaWFncmFtCiAgY2xhc3MgZGphbmdvX2NvbnRyaWJfYXV0aF9tb2RlbHNfVXNlclsiZGphbmdvLmNvbnRyaWIuYXV0aC5tb2RlbHM6OlVzZXIiXQogIGRqYW5nb19kYl9tb2RlbHNfdXRpbHNfQWx0ZXJzRGF0YSA8fC0tIGRqYW5nb19kYl9tb2RlbHNfYmFzZV9Nb2RlbAogIGNsYXNzIGRqYW5nb19kYl9tb2RlbHNfdXRpbHNfQWx0ZXJzRGF0YVsiZGphbmdvLmRiLm1vZGVscy51dGlsczo6QWx0ZXJzRGF0YSJdCiAgZGphbmdvX2NvbnRyaWJfYXV0aF9iYXNlX3VzZXJfQWJzdHJhY3RCYXNlVXNlciA8fC0tIGRqYW5nb19jb250cmliX2F1dGhfbW9kZWxzX0Fic3RyYWN0VXNlcgogIGRqYW5nb19jb250cmliX2F1dGhfbW9kZWxzX1Blcm1pc3Npb25zTWl4aW4gPHwtLSBkamFuZ29fY29udHJpYl9hdXRoX21vZGVsc19BYnN0cmFjdFVzZXIKICBjbGFzcyBkamFuZ29fY29udHJpYl9hdXRoX21vZGVsc19BYnN0cmFjdFVzZXJbImRqYW5nby5jb250cmliLmF1dGgubW9kZWxzOjpBYnN0cmFjdFVzZXIiXQogIGNsYXNzIGRqYW5nb19kYl9tb2RlbHNfYmFzZV9Nb2RlbFsiZGphbmdvLmRiLm1vZGVscy5iYXNlOjpNb2RlbCJdCiAgY2xhc3MgZGphbmdvX2NvbnRyaWJfYXV0aF9iYXNlX3VzZXJfQWJzdHJhY3RCYXNlVXNlclsiZGphbmdvLmNvbnRyaWIuYXV0aC5iYXNlX3VzZXI6OkFic3RyYWN0QmFzZVVzZXIiXQogIGRqYW5nb19kYl9tb2RlbHNfYmFzZV9Nb2RlbCA8fC0tIGRqYW5nb19jb250cmliX2F1dGhfYmFzZV91c2VyX0Fic3RyYWN0QmFzZVVzZXIKICBkamFuZ29fZGJfbW9kZWxzX2Jhc2VfTW9kZWwgPHwtLSBkamFuZ29fY29udHJpYl9hdXRoX21vZGVsc19QZXJtaXNzaW9uc01peGluCiAgZGphbmdvX2NvbnRyaWJfYXV0aF9tb2RlbHNfQWJzdHJhY3RVc2VyIDx8LS0gZGphbmdvX2NvbnRyaWJfYXV0aF9tb2RlbHNfVXNlcgogIGNsYXNzIGRqYW5nb19jb250cmliX2F1dGhfbW9kZWxzX1Blcm1pc3Npb25zTWl4aW5bImRqYW5nby5jb250cmliLmF1dGgubW9kZWxzOjpQZXJtaXNzaW9uc01peGluIl0="/>


