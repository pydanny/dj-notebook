# Contributing

TODO - improve and break into seperate files

## Development

Install the package in editable mode with test dependencies:

```bash
pip install -e '.[test]'
```

### Code quality

```bash 
make lint
```

### Testing

```bash
make test
```

### Releasing on PyPI

1. Update the `version` in `pyproject.toml`. We use semantic versioning
2. At the command line, run `make tag`
3. Go to [tags page](https://github.com/pydanny/dj_notebook/tags), choose the most recent tag, and click `Draft a new release`


### Building the project locally

Go to the project root

```bash
pip install --upgrade build
python -m build
```

Test the project, forcing reinstall if necessary

```bash
pip install dist/*.whl --force-reinstall
```

# Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [simplicuty](https://github.com/pydanny/simplicity) project template.
