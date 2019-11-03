#!/bin/bash

echo -e $(./frafeed.py get_entries_unread_short | jq -rf examples/terminal-short.jq) | less -R
