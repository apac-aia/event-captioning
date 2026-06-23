#!/usr/bin/env bash
# Rebuild enhanced.md + the three HTML variants (plain / desktop / mobile).
# Run after editing the source .md, CSS, or partials/.
set -euo pipefail
cd "$(dirname "$0")"

TITLE="台北場地現場人工智慧字幕與多語翻譯：ADALS 2026 白話操作報告"

python build-report-variants.py

common=(
  ai-captioning-ballroom-solution.enhanced.md
  -s --toc --toc-depth=3
  --metadata pagetitle="$TITLE"
  --include-before-body=partials/skiplink.html
  --include-after-body=partials/nav.html
  -c report-enhanced.css
)

pandoc "${common[@]}" -o ai-captioning-ballroom-solution.html
pandoc "${common[@]}" -c report-desktop.css -o ai-captioning-ballroom-solution.desktop.html
pandoc "${common[@]}" -c report-mobile.css -o ai-captioning-ballroom-solution.mobile.html

echo "built 3 HTML variants"
