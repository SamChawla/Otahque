# Otahque

An open-source, multi-tenant community CMS built with Django 6 and Python 3.12.

Named after the Sindhi word "Otaq" (اوطاق), a traditional community gathering
house. One account, many communities. Each community gets its own subdomain, its
own schema, its own theme, and a job board that refuses to print the word
"competitive".

This repository is built in public, one chapter at a time, alongside the book
[Django 6: Zero to Production Mastery](book/). Every chapter of the book has a
matching branch here, so you can check out the exact state of the code at the
end of any chapter.

## Status

Under construction. Chapter branches land one at a time.

| Branch | Contains |
|--------|----------|
| `main` | Repository scaffolding and the book submodule |
| `chapter-NN` | The project as it stands at the end of chapter NN |

## Getting the code

The book is a git submodule, so clone with `--recurse-submodules`:

```bash
git clone --recurse-submodules https://github.com/SamChawla/Otahque.git
cd Otahque
```

Already cloned without it?

```bash
git submodule update --init --recursive
```

## Running it

```bash
# Linux, macOS, Windows: uv handles the virtualenv and the Python version
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Full setup, including PostgreSQL and the multi-tenant schemas, is covered in the
book.

## The stack

Django 6 · Python 3.12 · PostgreSQL · Redis · DRF · Django Channels ·
Tailwind CSS 4 · daisyUI 5 · HTMX · Alpine.js · uv · ruff · pytest-django ·
Docker · Nginx · Gunicorn

No React, no Vue, no Node build step. Django templates render the HTML, HTMX
swaps the fragments, Alpine holds the small client-side state.

## The book

`book/` is a submodule pointing at the public book repository. Chapters are
released there one at a time so readers can send corrections as pull requests.
Every merged correction is credited in the acknowledgements and in the printed
book.

## Contributing

Corrections to the book go to the [book repository](book/). Issues and pull
requests against the code are welcome here.

## Licence

Code is MIT, see [LICENSE](LICENSE). The book text carries its own licence,
declared in the book repository.
