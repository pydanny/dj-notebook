changelog:  # Install gh cli and jq first
	gh api \
	-H "Accept: application/vnd.github+json" \
	-H "X-GitHub-Api-Version: 2022-11-28" \
	/repos/pydanny/dj-notebook/releases/latest > changelog.json
	
	python utils/update_changelog.py
	rm changelog.json

format:
	black .
	ruff check . --fix

lint:
	black .
	ruff check .

mypy:
	mypy .

VERSION=v$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

tag:
	echo "Tagging version $(VERSION)"
	git tag -a $(VERSION) -m "Creating version $(VERSION)"
	git push origin $(VERSION)


test:
	coverage run -m pytest .
	coverage report -m
	coverage html

install:
	pip install -e '.[dev]'
