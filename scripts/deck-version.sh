#!/usr/bin/env bash
# Print a deck's current version: the first "## x.y.z" heading in decks/<deck>/CHANGELOG.md.
#   scripts/deck-version.sh german   ->   2.0.0
set -euo pipefail
cd "$(dirname "$0")/.."
deck=${1:?usage: scripts/deck-version.sh <deck folder>}
version=$(grep -m1 -oE '^## [0-9]+\.[0-9]+\.[0-9]+' "decks/$deck/CHANGELOG.md" | cut -c4-) || true
[ -n "$version" ] || { echo "decks/$deck/CHANGELOG.md has no '## x.y.z' heading" >&2; exit 1; }
echo "$version"
