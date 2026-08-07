# illustration_only/manual_config.py
# Educational illustration only. This is the IDEA behind python-decouple,
# not its real implementation.

import os


class Undefined:
    """Sentinel meaning 'no default was given, so this value is required'."""


_UNDEFINED = Undefined()


def config(key: str, default: object = _UNDEFINED, cast: type = str) -> object:
    """Read `key` from the environment, applying a default and a type cast."""
    if key in os.environ:
        raw = os.environ[key]
    elif not isinstance(default, Undefined):
        raw = default
    else:
        raise KeyError(f"Required setting {key!r} is not set and has no default")

    if cast is bool:
        return str(raw).strip().lower() in {"1", "true", "yes", "on"}
    return cast(raw)


if __name__ == "__main__":
    os.environ["DEBUG"] = "true"
    print(config("DEBUG", default=False, cast=bool))   # True
    print(config("TIMEOUT", default="30", cast=int))    # 30
    print(config("SECRET_KEY"))                          # raises KeyError
