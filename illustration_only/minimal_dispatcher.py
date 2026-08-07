# illustration_only/minimal_dispatcher.py
# Educational illustration only. This is the IDEA behind Django's resolver,
# not its real implementation.

from collections.abc import Callable

# In this toy, a "request" is a dict and a "view" returns a string body.
Request = dict[str, str]
View = Callable[[Request], str]


def home_view(request: Request) -> str:
    return "<h1>Otahque</h1>"


def about_view(request: Request) -> str:
    return "<h1>About Otahque</h1>"


# The URL table: an ordered list of (path, view) pairs. Order decides priority.
URLPATTERNS: list[tuple[str, View]] = [
    ("/", home_view),
    ("/about/", about_view),
]


def resolve(path: str) -> View | None:
    """Return the first view whose pattern matches, or None for a 404."""
    for pattern, view in URLPATTERNS:
        if pattern == path:
            return view
    return None


def dispatch(path: str) -> str:
    """Find the view for a path and call it, or return a 404 body."""
    request: Request = {"path": path, "method": "GET"}
    view = resolve(path)
    if view is None:
        return "404 Not Found"
    return view(request)


if __name__ == "__main__":
    print(dispatch("/"))          # <h1>Otahque</h1>
    print(dispatch("/about/"))    # <h1>About Otahque</h1>
    print(dispatch("/missing/"))  # 404 Not Found
