# 台北字幕活動選型工具 + 完整報告

互動式選型工具，幫在台北辦活動的人快速篩出適合的場地，並推薦現場人工智慧字幕／多語翻譯工具與方案等級。附一份完整操作報告作為深入參考。

## 線上版（GitHub Pages）

- 選型工具：`index.html`（站台首頁）
- 完整報告（桌面版）：`ai-captioning-ballroom-solution.desktop.html`
- 完整報告（手機版）：`ai-captioning-ballroom-solution.mobile.html`

## 內容

| 檔案 | 說明 |
|---|---|
| `index.html` | 互動選型工具（單檔自包含，原生 JS，無相依） |
| `ai-captioning-ballroom-solution.md` | 完整報告原始檔（source of truth） |
| `ai-captioning-ballroom-solution.enhanced.md` | 加上導覽與章節重點的中繼檔（由 build 產生） |
| `ai-captioning-ballroom-solution.{,desktop,mobile}.html` | 報告三種版本（pandoc 產生） |
| `ai-captioning-ballroom-sources.md` | 來源索引 |
| `report-*.css` | 報告樣式 |
| `partials/` | 報告的 skip link 與導覽 JS（build 時內嵌） |
| `build-report-variants.py` / `build-html.sh` | 報告重建腳本 |

## 重建報告

改 `ai-captioning-ballroom-solution.md`、CSS 或 `partials/` 後：

```bash
bash build-html.sh
```

需要 `pandoc` 與 `python`。工具 `index.html` 是手寫單檔，直接編輯即可。

## 資料說明

場地公開價格為 2026-06 查詢的第一輪比較，非簽約價；正式採購仍須向場地與廠商確認，尤其「混音器能否提供只含人聲的乾淨訊號」這項關鍵需求。
