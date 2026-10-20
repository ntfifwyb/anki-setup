#!/usr/bin/env bash
# Build a deck and publish its .apkg on the deck's GitHub Release, whose tag is the deck's
# folder name (english-expressions). The tag moves to the current commit, so the download
# link stays the same: releases/download/<deck>/<file>.apkg
#   scripts/publish-deck.sh english-expressions
set -euo pipefail
cd "$(dirname "$0")/.."
deck=${1:?usage: scripts/publish-deck.sh <deck folder>}
[ -z "$(git status --porcelain)" ] || { echo "commit your changes first" >&2; exit 1; }
uv run --no-project -q -p 3.13 --with genanki==0.13.1 python "decks/$deck/build.py"
apkg=$(ls "decks/$deck"/*.apkg)
git tag -f "$deck" HEAD
git push -f origin "refs/tags/$deck"
notes="Built from $(git rev-parse --short HEAD). Open the .apkg with Anki to import or update the deck."
if gh release view "$deck" >/dev/null 2>&1; then
  gh release edit "$deck" --notes "$notes"
  gh release upload "$deck" "$apkg" --clobber
else
  gh release create "$deck" "$apkg" --title "$(head -1 "decks/$deck/README.md" | sed 's/^# //')" --notes "$notes"
fi
