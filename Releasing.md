# Releasing on PyPI

1. Update the `version` in `pyproject.toml`. We use semantic versioning
2. Create and push pull request branch called `release-x.x.x`
3. At the command line, run `make tag`
4. Go to [tags page](https://github.com/pydanny/dj-notebook/tags), choose the most recent tag, and click `Draft a new release`
5. Click `Generate release notes` and then `Publish release notes`
6. Run `make changelog`
7. Use `git commit --amend` to add the just pulled release notes to the release commit
8. `git push --force`
9. Merge to main