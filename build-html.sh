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

# Sources index as its own styled HTML page.
pandoc ai-captioning-ballroom-sources.md \
  -s --toc --toc-depth=2 \
  --metadata pagetitle="ADALS 2026 來源索引" \
  --include-before-body=partials/skiplink-sources.html \
  --include-after-body=partials/nav.html \
  -c report-enhanced.css \
  -o ai-captioning-ballroom-sources.html

# Post-event recording and caption workflow as a standalone maintained article.
pandoc video-caption-postproduction.md \
  -s --toc --toc-depth=2 \
  --metadata pagetitle="活動結束後：把 Zoom／直播錄影整理成可發布的影片字幕" \
  --metadata lang="zh-Hant" \
  --include-in-header=partials/video-caption-head.html \
  --include-after-body=partials/nav.html \
  -c report-enhanced.css \
  -c report-desktop.css \
  -c video-caption-postproduction.css \
  -o video-caption-postproduction.html

echo "built 3 report HTML variants + sources page + video caption article"
