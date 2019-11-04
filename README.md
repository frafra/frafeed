# Setup

Requirements: [Poetry](https://poetry.eustace.io/) and Python 3.7 or greater.

```
poetry shell
poetry install
```

# How to use

Help:

```
./frafeed.py --help
```

Example:
```
./frafeed.py add_feed http://rss.slashdot.org/Slashdot/slashdotMain
./frafeed.py update
./frafeed.py get_entries_unread_short
./frafeed.py mark_all_as_read
```

# Pretty printing

Requires [jq](https://stedolan.github.io/jq/).

```
./examples/terminal.sh
```

# How to extend it

Add your own SQL queries under `sql/`: they will automatically be exposed as Python functions and they will appear in `frafeed.py --help`.
