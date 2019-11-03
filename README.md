# Setup

Requirements: [Poetry](https://poetry.eustace.io/) and Python 3.7 or greater.

```
poetry run poetry install
```

# How to use

Help:

```
poetry run -- python frafeed.py --help
```

Example:
```
poetry run -- python frafeed.py add_feed http://rss.slashdot.org/Slashdot/slashdotMain
poetry run -- python frafeed.py get_entries_unread_short
poetry run -- python frafeed.py mark_all_as_read
```

# How to extend it

Add your own SQL queries under `sql/`: they will automatically be exposed as Python functions and they will appear in `frafeed.py --help`.
