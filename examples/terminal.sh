#!/bin/bash

echo -e $(./frafeed.py get_entries_unread | jq -rf examples/terminal.jq) | less -R
