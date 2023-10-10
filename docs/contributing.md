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

Code away!

### Standards

dj-notebook follows these standards:

- Styleguide: [PEP-8](https://peps.python.org/pep-0008/)
- Code of Conduct: [Contributor Covenant](https://www.contributor-covenant.org)
- Boring Technology for Packaging: setuptools and build

### Code quality

Linting and formatting is done with Black and Ruff:

```bash 
make lint
```

### Testing

```bash
make test
```

---
## Advanced

Odds are you won't need these things.

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


