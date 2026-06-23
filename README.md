# 字幕活動場地選型工具 + 完整報告（event-captioning）

幫在台北與新北（雙北）辦活動的人，快速篩出適合的場地，並推薦現場人工智慧字幕／多語翻譯工具與方案等級。附一份完整操作報告作為深入參考。以 ADALS 2026 為示範情境，任何雙北活動都可使用。

---

## 線上連結（GitHub Pages）

| 連結 | 內容 |
|---|---|
| https://apac-aia.github.io/event-captioning/ | 互動選型工具（站台首頁，`index.html`） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.desktop.html | 完整報告 桌面版（左側固定目錄） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.mobile.html | 完整報告 手機版（浮動目錄鈕） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-solution.html | 完整報告 純版（單欄） |
| https://apac-aia.github.io/event-captioning/ai-captioning-ballroom-sources.html | 來源索引（所有公開價格與官方連結） |

工具內與報告內的互連：工具頁右側／底部有「完整報告」連結；報告開頭與第 22 節連到「來源索引」；報告第 0 節為章節導覽，最前面是「決策頁」。

GitHub repo：`apac-aia/event-captioning`（public）。本機開發目錄：`C:/Code/apac-aia-captioning-tool/`；報告原始與重建在 `C:/Code/published-reports/adals/`（兩處需同步）。

---

## 檔案結構

| 檔案 | 說明 |
|---|---|
| `index.html` | 互動選型工具，單檔自包含、原生 JS、無外部相依。場地資料是檔內的 `VENUES` 陣列 |
| `ai-captioning-ballroom-solution.md` | 完整報告原始檔（source of truth），最前面含「決策頁」 |
| `ai-captioning-ballroom-solution.enhanced.md` | 加上導覽與章節重點的中繼檔（由 `build-report-variants.py` 產生） |
| `ai-captioning-ballroom-solution.{,desktop,mobile}.html` | 報告三版（pandoc 產生，含 scroll-spy 側欄、手機浮動目錄、back-to-top、skip link） |
| `ai-captioning-ballroom-sources.md` / `.html` | 來源索引原始檔與網頁 |
| `report-*.css` | 報告樣式（enhanced 共用、desktop/mobile/print 各自加掛） |
| `partials/` | 報告與來源頁的 skip link 與導覽 JS（build 時內嵌） |
| `build-report-variants.py` / `build-html.sh` | 報告重建腳本 |
| `.nojekyll` | 讓 Pages 直接輸出檔案、不經 Jekyll |

---

## 怎麼用工具

1. **前置設定 3 題**：活動人數規模（XS／S／M／L）、預算傾向（省／平衡／不限）、字幕定位（便利補充／正式無障礙服務）。
2. **看推薦卡**：依人數給方案等級與字幕工具；選「正式無障礙服務」會提醒「不能只靠 AI、需加 CART／手語」。
3. **左側即時微調**：場地類型、地點（北市／新北）、排除明確不可外接的場地、只看有公開價格、排除規模不合的場地。
4. **場地卡**：名稱、價格、容量／類型／字幕友善度標章、備註、官方來源連結。

---

## 重要注意事項

### 1. 價格與容量都是「比較起點」，不是定案
公開價格為 2026-06 查詢的第一輪比較，會因日期、人數、餐飲、稅金、服務費、假日、檔期、設備而變動。**正式採購前一定要向場地與廠商重新確認。** 各場地計價方式不同（每時段／每人／每日／每場）：飯店多為每人計價、人數越多總價越大；會議中心多為每時段、與人數較無關。比較時要換算成同一份總成本。

### 2. 成敗關鍵：乾淨人聲訊號
現場字幕成不成功，不在用哪個 App，而在場地的混音器能不能給字幕電腦一條「只含人聲的乾淨訊號」。**每個場地、不分工具，都要先問這件事。**

### 3. 正式無障礙服務不能只靠 AI
如果已知有聾人或聽障與會者需要字幕才能參與，人工智慧字幕不足，必須加 CART（即時人工字幕／同步聽打）、手語或專業字幕。這一點不分人數規模。工具的「字幕定位」選「正式無障礙服務」時會提醒。

### 4. 特定場地的已知限制
- **集思交通部國際會議廳**：劇院型約 76 人、教室型約 117 人，屬中小型，**坐不下 150-300 人**；適合 S 級小型活動，不是 M 級首選。M 級首推容量真的吃得下的 **集思台大會議中心**（劇院約 400 席）。
- **不可外接字幕設備（或受限）**：TICC、臺大醫院國際會議中心（同步翻譯設備不得自備）、臺大圖書館國際會議廳（無法外接其他影音）。需現場接字幕電腦者要特別確認，工具勾「排除明確不可外接的場地」會濾掉明確受限者。
- **無公開價（需詢價）**：萬豪、晶華、圓山、國泰萬怡、寒舍艾美、艾麗希爾頓格芮、大巨蛋、小巨蛋等。工具勾「只看有公開價格」會濾掉。台北新板希爾頓只有個案報價、非公開價。
- **容量待確認**：台北新板希爾頓（官方僅列 1,037 平方公尺、非人數）、台北艾麗希爾頓格芮（來源混用艾麗／Humble House，宴會廳另有資料稱近千人）。工具備註已標「需確認」。
- **賽事級巨蛋**：台北大巨蛋（約 4 萬席）、台北小巨蛋（約 1.5 萬席）為演唱會／賽事場地，列為對照，**不適合作會議主場**。

### 5. 工具與報告的定位差異（刻意）
- **工具**是通用的：給任何雙北活動主辦用，「字幕定位」預設為「便利補充」（多數活動的常見情況）。
- **報告決策頁**以 ADALS（無障礙活動）為示範，預設為「正式無障礙服務」，因此帶 CART／手語的提醒。
兩者預設不同是因為服務對象不同，不是矛盾。

---

## 資料來源與查證

- 完整來源（官方頁、價格、可信度）見「來源索引」頁。
- 本專案於 **2026-06-24** 經 codex 與 Claude 各兩輪交叉 review（價格、方案、文字、連結、一致性）。已修正：集思北科大感恩廳價格錯置、集思交通部容量高估、決策頁與無障礙原則的自相矛盾、台北新板希爾頓個案價誤標公開價等。
- **仍待人工確認的殘留項**：國立臺北商業大學、客家文化主題公園劇場、臺北表演藝術中心 的容量這次未逐一 live 複查；台北艾麗／Humble House 的品牌與容量對應仍待釐清。對外正式引用前建議再查證。

---

## 重建

改了 `ai-captioning-ballroom-solution.md`、CSS 或 `partials/` 後：

```bash
bash build-html.sh
```

會先跑 `build-report-variants.py` 產生 enhanced.md，再用 pandoc 產生報告三版 HTML 與來源頁。需要 `pandoc` 與 `python`。工具 `index.html` 是手寫單檔，直接編輯即可（場地資料在 `VENUES` 陣列）。

> 注意：報告檔同時存在 `C:/Code/published-reports/adals/`（開發）與本 repo（部署），改完要同步兩處。

---

## 維運注意

- 推送用 `gh auth switch --user chiehweihuang`（active 帳號會自己切回 devBrightRaven，每次推送前重切）；commit identity 為 Bertram Huang <chieh.wei.huang@gmail.com>。
- 遠端有一條空的 `master` 殘留分支（預設分支已是 `main`），因 `git push --delete` 與 `gh api -X DELETE` 被本機 deny-list 擋下未刪；要清的話到 GitHub repo 網頁 Branches 一鍵刪除即可。
