# dj-notebook

A Jupyter notebook with access to objects from the Django ORM is a powerful tool to introspect data and run ad-hoc queries. This works with modern Django and Python 3.9, 3.10, and 3.11.

## Features

- Easy ipython notebooks with Django
- Built-in integration with the imported objects from django-extensions
- Inheritance diagrams on any object, including ORM models
- Converts any Django QuerySet to Pandas Dataframe
- Handy function for displaying mermaid charts in 

## Installation

Use your installation tool of choice, here we use venv and pip:

```bash
python -m venv venv
source venv/bin/activate
pip install dj_notebook
```

## Usage

First, find your project's `manage.py` file and open it. Copy whatever is being set to `DJANGO_SETTINGS_MODULE` into your clipboard.

Create an ipython notebook in the same directory as `manage.py`. In VSCode,
simply add a new `.ipynb` file. If using Jupyter Lab, use the `File -> New ->
Notebook` menu option.

Then in the first cell enter:

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

## QuerySet to Dataframe

```python
plus.read_frame(plus.User.objects.all())
```

## Check out the official documentation for more things you can do!

[dj-notebook official documentation](https://dj-notebook.readthedocs.io/)


# Contributors

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/pydanny">
            <img src="https://avatars.githubusercontent.com/u/62857?v=4" width="100;" alt="pydanny"/>
            <br />
            <sub><b>Daniel Roy Greenfeld</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/skyforest">
            <img src="https://avatars.githubusercontent.com/u/13559970?v=4" width="100;" alt="skyforest"/>
            <br />
            <sub><b>Cody Antunez</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/anna-zhydko">
            <img src="https://avatars.githubusercontent.com/u/68199135?v=4" width="100;" alt="anna-zhydko"/>
            <br />
            <sub><b>Anna Zhydko</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/bloodearnest">
            <img src="https://avatars.githubusercontent.com/u/1042?v=4" width="100;" alt="bloodearnest"/>
            <br />
            <sub><b>Simon Davy</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/akashverma0786">
            <img src="https://avatars.githubusercontent.com/u/138790903?v=4" width="100;" alt="akashverma0786"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/DaveParr">
            <img src="https://avatars.githubusercontent.com/u/8363743?v=4" width="100;" alt="DaveParr"/>
            <br />
            <sub><b>Dave Parr</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/specbeck">
            <img src="https://avatars.githubusercontent.com/u/98754084?v=4" width="100;" alt="specbeck"/>
            <br />
            <sub><b>Saransh Sood</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/syyong">
            <img src="https://avatars.githubusercontent.com/u/12908907?v=4" width="100;" alt="syyong"/>
            <br />
            <sub><b>Siew-Yit Yong</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

## Special thanks

[Tom Preston](github.com/prestto) did seminal work on Python paths that later became the foundation of dj-notebook.

[Evie Clutton](github.com/evieclutton) was co-author of a pull request that doesn't show up in the contributor list above.


<!-- readme: prestto,evieclutton -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/prestto">
            <img src="https://avatars.githubusercontent.com/u/13559801?v=4" width="100;" alt="prestto"/>
            <br />
            <sub><b>Tom Preston</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/evieclutton">
            <img src="https://avatars.githubusercontent.com/u/44432176?v=4" width="100;" alt="evieclutton"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: prestto,evieclutton -end -->



