# This very incomplete configuration allows unit tests to take the same path as a standard call
# to activate(). This one enables the test for a warning when DEBUG == False to pass.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

USE_TZ = True
DEBUG = False
