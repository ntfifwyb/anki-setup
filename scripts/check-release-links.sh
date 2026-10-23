#!/usr/bin/env bash
# Fail when a deck's download links don't point at its current version: every
# releases/download/<deck>-<version>/ and releases/tag/<deck>-<version> link in the root README
# and the deck's README must use the newest version in the deck's CHANGELOG.md, and both READMEs
# must have one. Run by .local-ci.
set -euo pipefail
cd "$(dirname "$0")/.."
status=0
for dir in decks/*/; do
  deck=$(basename "$dir")
  version=$(scripts/deck-version.sh "$deck") || { status=1; continue; }
  for readme in README.md "$dir/README.md"; do
    links=$(grep -oE "releases/(download|tag)/$deck[^/) ]*" "$readme" || true)
    if ! grep -qx "releases/download/$deck-$version" <<<"$links"; then
      echo "$readme: no download link for $deck $version" >&2; status=1
    fi
    stale=$(grep -vxE "releases/(download|tag)/$deck-$version" <<<"$links" || true)
    if [ -n "$stale" ]; then
      echo "$readme: links not at $deck $version:" $stale >&2; status=1
    fi
  done
done
[ $status -eq 0 ] && echo "download links match each deck's CHANGELOG.md"
exit $status
