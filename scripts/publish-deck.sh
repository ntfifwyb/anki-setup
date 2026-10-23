#!/usr/bin/env bash
# Build a deck and publish it as a new GitHub Release, so every version stays on the releases page.
# The version is the newest "## x.y.z" heading in the deck's CHANGELOG.md, the tag <deck>-x.y.z
# (german-2.0.0), the title the deck's name in its own language (its README's first line) and the
# notes that version's changelog section. Add the version to CHANGELOG.md and point the download
# links at it (scripts/check-release-links.sh checks them) in the PR, then publish after merging:
#   scripts/publish-deck.sh german
set -euo pipefail
cd "$(dirname "$0")/.."
deck=${1:?usage: scripts/publish-deck.sh <deck folder>}
changelog="decks/$deck/CHANGELOG.md"
[ -z "$(git status --porcelain)" ] || { echo "commit your changes first" >&2; exit 1; }
version=$(scripts/deck-version.sh "$deck")
tag="$deck-$version"
if gh release view "$tag" >/dev/null 2>&1; then
  echo "$tag is already published: add a new version to $changelog" >&2; exit 1
fi
uv run --no-project -q -p 3.13 --with genanki==0.13.1 python "decks/$deck/build.py"
apkg=$(ls "decks/$deck"/*.apkg)
# The section under the newest version heading, up to the next one.
changes=$(awk '/^## /{n++; next} n==1' "$changelog")
notes="$changes

Built from $(git rev-parse --short HEAD). Open the .apkg with Anki to import or update the deck."
git tag "$tag" HEAD
git push origin "refs/tags/$tag"
gh release create "$tag" "$apkg" --title "$(head -1 "decks/$deck/README.md" | sed 's/^# //') $version" --notes "$notes"
