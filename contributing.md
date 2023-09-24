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
2. Create and merge a PR branch called `release-x.x.x`
3. Pull from `main``
4. At the command line, run `make tag`
5. Go to [tags page](https://github.com/pydanny/listo/tags), choose the most recent tag, and click `Draft a new release`
6. Click `Generate release notes` and save
7. Run `make changelog`
8. Use `git commit --amend` to add the just pulled release notes to the release commit


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
