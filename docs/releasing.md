# Releasing on PyPI

1. Update the `version` in `pyproject.toml` and `__version__` in` `src/__init__.py`. We use semantic versioning
2. Create a branch called `release-x.x.x`
3. At the command line, run `make tag`
4. Go to [tags page](https://github.com/pydanny/dj-notebook/tags), choose the most recent tag, and click `Draft a new release`
5. Click `Generate release notes` and then `Publish release notes`
6. Run `make changelog`
7. Use `git commit` and `git push` any files changed by this release
8. Send up with `git push origin release-x.x.x`
9. Merge to main