# Contributing

## Git workflow

* Fork the repository
* Make your changes in your fork
* Open a pull request to upstream repository - main branch

## Development

Install the package in editable mode with test dependencies:

```bash
pip install -e '.[test]'
```

### Code quality

Lint to codebase with black and ruff for code formatting and linting:

```bash 
make lint
```

### Testing

```bash
make test
```

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

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [simplicity](https://github.com/pydanny/simplicity) project template.
