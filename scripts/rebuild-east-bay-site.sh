#!/usr/bin/env bash
# Rebuild the eastbayservices.com static site from its public pages into a local folder.
# Usage: scripts/rebuild-east-bay-site.sh [output-dir]
set -euo pipefail

SITE="https://eastbayservices.com"
OUT="${1:-east-bay-services}"
UA="EastBayRebuild/1.0 (+hello@eastbayservices.com)"

mkdir -p "$OUT"
cd "$OUT"

curl -fsS -A "$UA" "$SITE/robots.txt" -o robots.txt
if grep -qiE '^Disallow:\s*/\s*$' robots.txt; then
  echo "robots.txt disallows crawling; stopping." >&2
  exit 1
fi
curl -fsS -A "$UA" "$SITE/sitemap.xml" -o sitemap.xml

# The nav is built in JavaScript, so wget cannot discover every page by following links.
{
  grep -oE '<loc>[^<]+' sitemap.xml | sed 's/<loc>//'
  printf '%s\n' \
    "$SITE/f/" \
    "$SITE/f/new/" \
    "$SITE/data/metro-registry.json" \
    "$SITE/data/empty-states.json" \
    "$SITE/images/favicon.svg" \
    "$SITE/images/app-icon-star-in-navy.svg" \
    "$SITE/images/mark-star-in-navy.svg"
} | sort -u > urls.txt

wget --mirror --page-requisites --no-parent --no-host-directories \
  --wait=0.5 --user-agent="$UA" --input-file=urls.txt || true

rm -f urls.txt

missing=0
while read -r url; do
  path="${url#"$SITE"}"
  path="${path#/}"
  file="${path}index.html"
  [ -z "$path" ] && file="index.html"
  if [ ! -s "$file" ]; then
    echo "MISSING: $url -> $file" >&2
    missing=1
  fi
done < <(grep -oE '<loc>[^<]+' sitemap.xml | sed 's/<loc>//')

for f in js/config.js js/site.js js/work-file.js css/site.css css/work-file.css; do
  if [ ! -s "$f" ]; then
    echo "MISSING: $f" >&2
    missing=1
  fi
done

echo "files: $(find . -type f | wc -l)"
exit "$missing"
