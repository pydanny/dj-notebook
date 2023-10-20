from os import environ

if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "bar.settings")