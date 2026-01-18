#!/bin/bash
set -e
uv sync
. .venv/bin/activate
MODULES=$(/usr/bin/comm -12 <(.venv/bin/manifestoo --select-found --exclude-core-addons list) <(.venv/bin/manifestoo -d . list-depends))
mkdir -p vendor
while IFS= read -r file; do
    echo "Processing file: $file"
    rsync -r --delete .venv/lib/python3.12/site-packages/odoo/addons/$file vendor/
    # Add your commands here
done <<< "$MODULES"
