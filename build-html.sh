#!/usr/bin/env bash
# Rebuild enhanced.md + the three HTML variants (plain / desktop / mobile).
# Run after editing the source .md, CSS, or partials/.
set -euo pipefail
cd "$(dirname "$0")"

TITLE="ADALS 2026 場地與字幕執行案例"

if command -v python >/dev/null 2>&1; then
  PYTHON=(python)
elif command -v python3 >/dev/null 2>&1; then
  PYTHON=(python3)
elif command -v py >/dev/null 2>&1; then
  PYTHON=(py -3)
elif [[ -x /c/Windows/py.exe ]]; then
  PYTHON=(/c/Windows/py.exe -3)
else
  echo "Python 3 is required to build the report variants." >&2
  exit 1
fi

if command -v pandoc >/dev/null 2>&1; then
  PANDOC=(pandoc)
elif command -v powershell.exe >/dev/null 2>&1; then
  PANDOC_WIN="$(powershell.exe -NoProfile -Command '(Get-Command pandoc -ErrorAction SilentlyContinue).Source' | tr -d '\r')"
  if command -v wslpath >/dev/null 2>&1; then
    PANDOC_EXE="$(wslpath -u "$PANDOC_WIN")"
  elif command -v cygpath >/dev/null 2>&1; then
    PANDOC_EXE="$(cygpath -u "$PANDOC_WIN")"
  else
    PANDOC_EXE=""
  fi
  if [[ -n "$PANDOC_WIN" && -x "$PANDOC_EXE" ]]; then
    PANDOC=("$PANDOC_EXE")
  else
    echo "Pandoc is required to build the HTML pages." >&2
    exit 1
  fi
else
  echo "Pandoc is required to build the HTML pages." >&2
  exit 1
fi

"${PYTHON[@]}" build-report-variants.py

common=(
  ai-captioning-ballroom-solution.enhanced.md
  -s --toc --toc-depth=3
  --metadata pagetitle="$TITLE"
  --metadata lang="zh-Hant"
  --include-in-header=partials/report-head.html
  --include-before-body=partials/report-main-open.html
  --include-after-body=partials/report-main-close.html
  --include-after-body=partials/nav.html
  -c report-enhanced.css
)

"${PANDOC[@]}" "${common[@]}" -o ai-captioning-ballroom-solution.html
"${PANDOC[@]}" "${common[@]}" -c report-desktop.css -o ai-captioning-ballroom-solution.desktop.html
"${PANDOC[@]}" "${common[@]}" -c report-mobile.css -o ai-captioning-ballroom-solution.mobile.html

# ai-captioning-ballroom-sources.html contains a manually maintained expanded
# venue index that is not represented in the Markdown source. Do not overwrite it here.

# Post-event recording and caption workflow as a standalone maintained article.
"${PANDOC[@]}" video-caption-postproduction.md \
  -s --toc --toc-depth=2 \
  --metadata pagetitle="活動錄影完成後，字幕接下來怎麼處理？" \
  --metadata lang="zh-Hant" \
  --include-in-header=partials/video-caption-head.html \
  --include-after-body=partials/nav.html \
  -c report-enhanced.css \
  -c report-desktop.css \
  -c video-caption-postproduction.css \
  -o video-caption-postproduction.html

echo "built 3 report HTML variants + video caption article (sources page preserved)"
