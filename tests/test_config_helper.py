import pytest

from pathlib import Path
import os

from dj_notebook.config_helper import setdefault_calls, find_django_settings_module


class EnvironmentGuard:
    def __enter__(self):
        self.original_environment = {}
        for k in os.environ.keys():
            self.original_environment[k] = os.environ[k]
        return None
    def __exit__(self, exc_type, exc_val, exc_tb):
        for k in os.environ.keys():
            del os.environ[k]
        for k in self.original_environment.keys():
            os.environ[k] = self.original_environment[k]

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


def test_find_django_settings_module_dotenv():
    env_file = "env.django_settings_module"
    with EnvironmentGuard():
        source, found = find_django_settings_module(dotenv_file=Path(env_file))
        assert source == "dotenv"
        assert os.environ["DJANGO_SETTINGS_MODULE"] == found
        assert found == "bip.config"


def test_find_django_settings_module_dotenv_overrides():
    env_file = "env.django_settings_module"
    with EnvironmentGuard():
        os.environ["DJANGO_SETTINGS_MODULE"] = "something.else"
        source, found = find_django_settings_module(dotenv_file=Path(env_file))
        assert source == "dotenv"
        assert os.environ["DJANGO_SETTINGS_MODULE"] == found
        assert found == "bip.config"

def test_find_django_settings_module_os_environment():
    with EnvironmentGuard():
        os.environ["DJANGO_SETTINGS_MODULE"] = "something.else"
        source, found = find_django_settings_module()
        assert source == "environment"
        assert os.environ["DJANGO_SETTINGS_MODULE"] == found
        assert found == "something.else"
