import json
import pathlib
import typing


def main() -> None:
    changes: dict[str, typing.Any] = json.loads(
        pathlib.Path("changelog.json").read_text()
    )
    previous_changelog: str = pathlib.Path("CHANGELOG.md").read_text()

    new_changelog: str = f"""
# [{changes["tag_name"]}]({changes['html_url']})

{changes['created_at']} by
[@{changes['author']['login']}]({changes['author']['html_url']})

## {changes["body"]}

---

{previous_changelog}
"""

    pathlib.Path("CHANGELOG.md").write_text(new_changelog)


if __name__ == "__main__":
    main()
