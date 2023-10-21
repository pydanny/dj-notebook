class Environ:
    def setdefault(self, k: str, v: str) -> None:
        print(f"{k}={v}")


environ = Environ()

if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "foo.bar.settings")
