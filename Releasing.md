# Releasing on PyPI

1. Update the `version` in `pyproject.toml`. We use semantic versioning
2. Create and merge a pull request branch called `release-x.x.x`
3. Pull from `main`
4. At the command line, run `make tag`
5. Go to [tags page](https://github.com/pydanny/listo/tags), choose the most recent tag, and click `Draft a new release`
6. Click `Generate release notes` and save
7. Run `make changelog`
8. Use `git commit --amend` to add the just pulled release notes to the release commit