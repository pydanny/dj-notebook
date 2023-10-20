from os import environ as os_environ

if __name__ == "__main__":
    os_environ.setdefault("DJANGO_SETTINGS_MODULE", "baz.settings")