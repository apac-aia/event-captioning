# 活動字幕選型工具（event-captioning）

一個不綁定特定活動的字幕與混合活動選型工具。依活動條件整理場地、字幕工具、方案級距、成本、人力與無障礙提醒，場地範圍涵蓋全台。

第一次開啟時的設定只是操作範例。使用者更改條件後，推薦、警示、總覽與列印內容都會依目前選項更新。

## 線上版本

| 連結 | 內容 |
|---|---|
| https://apac-aia.github.io/event-captioning/ | 互動選型工具 |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.desktop.html | 場地與字幕執行手冊（桌面版） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.mobile.html | 場地與字幕執行手冊（手機版） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.html | 場地與字幕執行手冊（單欄版） |
| https://apac-aia.github.io/event-captioning/video-caption-postproduction.html | 會後錄影與影片字幕處理教學 |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-sources.html | 來源索引 |

## 使用方式

1. 設定活動規模、籌備時間、核心人力與當日技術人力。
2. 設定活動目的、收費模式、贊助狀態與預算傾向。
3. 選擇字幕定位、主要發言語言、目標字幕語言，以及是否需要錄影／回放。
4. 依人數、城市、場地類型與搜尋條件篩選場地。
5. 比較字幕工具，選定候選工具後到「總覽」檢查成本、人力與風險。

預設範例使用 `S（50-150）`、兩個月內、正式售票、已確認贊助、英文發言，以及繁中／日文字幕。這些不是所有活動的固定基準。

## 判斷原則

- **語言方向是選型條件**：工具會依「主要發言語言 -> 目標字幕語言」產生建議。供應商宣稱支援某語言，不代表同時支援該語言作為輸入與輸出。
- **錄影與即時字幕分開處理**：即時 AI 翻譯可服務當天觀眾；公開影片的翻譯字幕仍需另外產生並人工校對。
- **正式無障礙不能只靠 AI**：已知有聾人或聽障者需要字幕時，應安排 CART、同步聽打、手語或明確採購的人工專業字幕服務。
- **乾淨人聲優先**：場地必須能從混音器提供只含人聲的訊號給字幕系統，並把問答麥克風納入同一條音訊鏈路。
- **價格只是比較起點**：場租、影音、字幕工具與人力都要在採購前取得書面報價。

## 專案結構

| 檔案 | 說明 |
|---|---|
| `index.html` | 互動選型工具；原生 HTML、CSS、JavaScript，無前端相依 |
| `ai-captioning-ballroom-solution.md` | 場地與字幕執行手冊來源 |
| `ai-captioning-ballroom-solution.enhanced.md` | 報告建置中繼檔 |
| `ai-captioning-ballroom-solution.{,desktop,mobile}.html` | 場地與字幕執行手冊的三種版型 |
| `video-caption-postproduction.md` / `.html` | Zoom、Teams、Meet 與 YouTube 的會後字幕處理教學 |
| `ai-captioning-ballroom-sources.md` / `.html` | 資料來源索引 |
| `accessible-checklist.pdf` | 無障礙活動加辦清單 |
| `tool-summary.pdf` | 選型工具完整資料 |
| `report-*.css` | 報告共用、桌面、手機與列印樣式 |
| `partials/` | 報告建置時嵌入的導覽片段 |
| `build-report-variants.py` / `build-html.sh` | 報告重建腳本 |

## 本機使用與重建

互動工具是單檔頁面，可直接開啟 `index.html`。

修改報告來源、樣式或 `partials/` 後，使用具備 Python、Pandoc 與 Bash 的環境執行：

```bash
bash build-html.sh
```

## 維護注意

- 場地容量、價格、設備限制與供應商功能可能變動；更新資料時保留官方來源連結與查證日期。
- 不要把範例活動的預設條件寫成通用推薦。新的條件若會影響選型，應成為可調整的輸入或寫成明確條件句。
- 工具與場地／字幕執行手冊用途不同：工具依使用者目前設定產生建議；手冊提供背景研究、操作流程與來源脈絡。
