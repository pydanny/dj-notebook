import pytest

from pathlib import Path
import os

from dj_notebook.config_helper import setdefault_calls

def test_setdefault_calls_fully_qualified():
    script_dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    manage_py = script_dir_path / "fake_manage_fully_qualified.py"
    calls = list(setdefault_calls(manage_py))
    assert len(calls) == 1
    assert calls[0].args[0].value == "DJANGO_SETTINGS_MODULE"
    assert calls[0].args[1].value == "foo.settings"


def test_setdefault_calls_import_function():
    script_dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    manage_py = script_dir_path / "fake_manage_import_environ.py"
    calls = list(setdefault_calls(manage_py))
    assert len(calls) == 1
    assert calls[0].args[0].value == "DJANGO_SETTINGS_MODULE"
    assert calls[0].args[1].value == "bar.settings"


def test_setdefault_calls_import_alias():
    script_dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    manage_py = script_dir_path / "fake_manage_alias_environ.py"
    calls = list(setdefault_calls(manage_py))
    assert len(calls) == 1
    assert calls[0].args[0].value == "DJANGO_SETTINGS_MODULE"
    assert calls[0].args[1].value == "baz.settings"
