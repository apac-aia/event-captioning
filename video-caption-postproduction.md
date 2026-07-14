<a id="top"></a>
<a class="skip-link" href="#main-content">跳到文章內容</a>

<main id="main-content">

# 活動結束後：把 Zoom／直播錄影整理成可發布的影片字幕

**資料查核日期：2026-07-14。** 平台功能、授權與檔案格式可能調整；活動前仍要用實際帳號做一次完整測試。

<div class="version-switch" role="navigation" aria-label="相關頁面">
<a href="index.html">返回字幕選型工具</a>
<a href="ai-captioning-ballroom-solution.desktop.html">查看場地與字幕執行手冊</a>
</div>

## 先說結論

活動當天顯示的 AI 即時字幕或翻譯字幕，主要是幫助觀眾跟上現場。它通常不是可以直接公開的最終影片字幕。

比較穩定的會後流程是：

> 保留原始錄影與音訊 → 取得原語逐字稿或字幕檔 → 先校對原語 → 再翻譯 → 校對翻譯與時間碼 → 上傳獨立字幕軌 → 最後才公開影片

不要先翻譯一份錯誤很多的 AI 逐字稿。人名、組織、專有名詞與數字一旦在原語寫錯，錯誤會一起進入所有翻譯版本。

## 1. 活動前就要決定的五件事

### 1.1 指定一位會後字幕負責人

這個人不一定親自完成所有字幕，但要負責收齊檔案、確認校對者與翻譯者、管理版本，以及決定何時可以公開。

### 1.2 確認要交付哪些版本

至少先決定：

- 只保留內部回放，還是要公開上架。
- 需要原語字幕，還是要繁中、日文等翻譯字幕。
- 是否要交付贊助商、講者或未參加直播的人。
- 是否需要文字版逐字稿。
- 影片中的投影片、示範畫面或圖表是否包含只靠畫面才能理解的重要資訊。

### 1.3 先確認錄影、轉錄與保存權限

錄影和逐字稿通常受帳號方案、管理員政策、主持人角色與雲端空間影響。活動前要用真正負責錄影的帳號確認：

- 能否開始雲端錄影。
- 是否需要另外開啟 transcription／逐字稿。
- 誰能下載錄影與字幕檔。
- 錄影多久後會到期或被自動刪除。
- 參與者會收到什麼錄影或轉錄通知。

### 1.4 設定正確的主要發言語言

逐字稿引擎需要知道它正在辨識什麼語言。若活動以英文發言，就把原語逐字稿設為英文；不要把目標字幕語言「繁中」誤設成發言語言。

### 1.5 用五分鐘測試片段走完一次

測試片段要包含講者姓名、組織名稱、英文縮寫、數字、日文或中文詞彙，以及一段觀眾問答。活動前實際完成一次：錄影、停止、等待處理、下載逐字稿、修字、重新上傳字幕。

## 2. 活動結束後的標準流程

### 步驟 1：先封存原始檔

至少保留：

- 原始錄影檔。
- 原始音訊；平台能分軌時也保留分軌。
- 平台產生的原語逐字稿或 `VTT`。
- 當天使用的術語表、講者名單與議程。
- 即時字幕服務商可匯出的字幕或紀錄。

先複製一份唯讀備份，再開始剪輯或修字幕。

### 步驟 2：先鎖定影片時間軸

先完成片頭、片尾、休息段落、不能公開的內容與技術中斷剪除。影片長度改變後，舊字幕時間碼通常會對不上；因此不要在字幕全部校好後才大幅剪片。

### 步驟 3：校對原語字幕

優先修正會改變理解的錯誤：

- 講者姓名與組織名稱。
- 專有名詞、產品名稱與縮寫。
- 數字、日期、金額與網址。
- 否定詞，例如「可以／不可以」。
- 講者切換與問答段落。
- 重要聲音，例如 `[掌聲]`、`[笑聲]`、`[音訊中斷]`。

W3C 說明，字幕不只包含對話，也應包含理解內容所需的非語音資訊；自動字幕通常仍需要人工修正。

### 步驟 4：從校對後的原語翻譯

每一種語言建立獨立字幕檔，不要直接覆蓋原語字幕。翻譯者至少要取得：

- 已校對的原語字幕。
- 講者與組織正式譯名。
- 活動術語表。
- 影片或可核對語氣的音訊。

繁中與日文要各自校對，不要把當天未校對的即時翻譯直接改名成最終字幕。

### 步驟 5：檢查時間碼與可讀性

完整播放一次，至少檢查：

- 字幕沒有提早消失或晚很多才出現。
- 換行沒有把人名、數字或完整語意拆開。
- 畫面上的姓名、職稱與字幕用詞一致。
- 兩人對話時能知道誰在說話。
- 重要聲音與沒有語音的停頓沒有被誤寫成對話。
- 片頭、片尾與被剪除段落沒有殘留字幕。

### 步驟 6：以可開關的字幕軌發布

公開平台支援時，優先上傳獨立的 `SRT` 或 `VTT` 字幕軌，讓觀眾自行開關與選擇語言。除非發布平台不支援字幕軌，否則不要只把字幕燒死在畫面上。

## 3. Zoom：下載原語 VTT，再做翻譯版本

Zoom 的雲端錄影音訊轉錄會在處理完成後產生獨立 `VTT`。主持人可在 Zoom 網頁後台的 **Recordings & Transcripts → Cloud recordings** 找到錄影，檢視、編輯或下載逐字稿。

活動前要確認：

1. 主持帳號具備雲端錄影與 audio transcription 資格。
2. Cloud recording 與 audio transcription 已開啟。
3. 逐字稿的主要語言設定正確。
4. 活動結束後由誰登入、下載錄影與 `VTT`。

會後建議：

1. 下載原始影片、音訊與原語 `VTT`。
2. 先修正原語 `VTT`。
3. 另存繁中、日文等翻譯字幕檔。
4. 將各語言字幕上傳到最終播放平台。

**不要假設觀眾在會議中選到的 Translated Captions，活動後會自動變成可交付的翻譯字幕檔。** Zoom 官方雲端轉錄文件明確說明的是錄影音訊逐字稿與 `VTT`；因此實務上應把校對後的原語 `VTT` 當母檔，再製作翻譯版本。

官方文件：[Zoom 雲端錄影音訊轉錄](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064927)、[Zoom Translated Captions](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059081)。

## 4. Microsoft Teams：要開逐字稿，不只開即時字幕

Teams 的即時字幕只供會議當下觀看；它不會直接錄進下載的影片。若要留下可下載的文字，必須使用 recording／transcription 流程。

一般 Teams 會議：

- 錄影時會啟動轉錄；也可以只啟動 transcription。
- 會後由會議聊天的 **Recap → Transcript** 下載 `DOCX` 或 `VTT`。
- 官方說明指出，過去的 translated transcripts 不會被保存，只有原始逐字稿會保存。
- 非頻道會議錄影通常存放在主辦人的 OneDrive for Business；頻道會議則存放在 SharePoint。

因此會後流程仍是：下載原語 `VTT` → 校對 → 另做繁中／日文字幕。若使用 Teams Town Hall，其會後翻譯逐字稿另涉及 Microsoft 365、Clipchamp／Syntex 與管理員設定，不能直接套用一般會議假設。

官方文件：[Teams 啟動與下載逐字稿](https://support.microsoft.com/en-us/teams/meetings/start-stop-and-download-live-transcripts-in-microsoft-teams-meetings)、[Teams 錄影播放與下載](https://support.microsoft.com/en-us/teams/meetings/play-share-and-download-meeting-recordings-in-microsoft-teams)、[Town Hall 錄影與逐字稿](https://support.microsoft.com/en-us/teams/meetings/manage-town-hall-recordings-in-microsoft-teams)。

## 5. Google Meet：錄製字幕與獨立逐字稿是兩件事

Google Meet 錄影時可以選擇 **Record captions**，讓字幕能隨錄影播放。錄影與字幕處理完成時間可能不同，因此錄影先出現時，不代表字幕已經遺失。

Meet 的 **Transcripts** 是另一項功能。官方目前列出的逐字稿支援語言包括英文、法文、德文、義大利文、日文、韓文、葡萄牙文與西班牙文；繁中不在這份逐字稿支援清單內。逐字稿完成後會寄給主持人、共同主持人與啟動逐字稿的人，也會附在 Google Calendar 活動上。

若活動以英文發言、當天顯示繁中翻譯字幕：

1. 以英文逐字稿或錄製字幕作為原語材料。
2. 人工校對英文。
3. 再製作繁中與日文字幕。

不要把「Meet 當天能顯示繁中翻譯字幕」解讀成「會後一定能下載繁中逐字稿」。這兩項功能的語言支援與交付方式不同。

官方文件：[Google Meet 錄影](https://support.google.com/meet/answer/9308681)、[Google Meet Transcripts](https://support.google.com/meet/answer/12849897)、[Google Meet 翻譯字幕](https://support.google.com/meet/answer/10964115)。

## 6. YouTube：把每種語言當成獨立字幕軌

在 YouTube Studio 進入 **Subtitles → 選擇影片 → Add language → Add**，可以上傳已有時間碼的字幕檔，也可以貼上原語文字讓平台自動對時。

對活動錄影，建議直接上傳已校對的字幕檔：

- `SRT`：簡單、普遍，使用純文字 UTF-8。
- `VTT`：可保留時間碼，也能從 Zoom 或 Teams 的輸出開始整理。

YouTube 自動字幕只會以影片的預設語言產生，不能代替人工校對，也不能代替繁中、日文等翻譯字幕軌。

官方文件：[YouTube 新增字幕](https://support.google.com/youtube/answer/2734796)、[YouTube 支援的字幕格式](https://support.google.com/youtube/answer/2734698)。

## 7. 最終交付清單

一場需要會後回放的活動，至少應留下：

| 檔案 | 用途 |
|---|---|
| `event-master.mp4` | 完成剪輯的母片 |
| `event-source-en.vtt` | 已校對的原語字幕；檔名依實際語言調整 |
| `event-zh-Hant.srt` | 已校對的繁中字幕 |
| `event-ja.srt` | 已校對的日文字幕 |
| `event-transcript.docx` 或網頁逐字稿 | 搜尋、引用與不方便播放影片時閱讀 |
| `terminology.xlsx` 或 `terminology.csv` | 人名、組織、產品、縮寫與固定譯名 |
| `qa-notes.txt` | 記錄已知問題、校對者、版本與日期 |
| `permissions.txt` | 錄影、講者簡報、音樂及公開範圍的確認紀錄 |

若影片中的投影片、圖表或示範動作包含單靠語音無法理解的重要資訊，還要提供口述影像或描述性逐字稿。W3C 建議字幕涵蓋語音與重要非語音聲音，並另外處理理解內容所需的視覺資訊。

## 8. 公開前最後檢查

- [ ] 影片已完成剪輯，之後不再改時間軸。
- [ ] 原語字幕已由人看過，不只跑拼字檢查。
- [ ] 人名、組織、數字、日期與網址正確。
- [ ] 每種翻譯字幕都從已校對原語產生。
- [ ] 每種語言都在實際播放器開啟測試。
- [ ] 字幕可以用鍵盤開關與切換語言。
- [ ] 逐字稿或字幕下載位置容易找到。
- [ ] 錄影、簡報、音樂與參與者公開範圍已確認。
- [ ] 若有重要視覺資訊，已有口述或文字描述。
- [ ] 原始檔、發布檔與字幕版本已備份。

## 參考資料

- [W3C WAI：Captions/Subtitles](https://www.w3.org/WAI/media/av/captions/)
- [W3C WAI：Transcripts](https://www.w3.org/WAI/media/av/transcripts/)
- [Zoom：Using audio transcription for cloud recordings](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064927)
- [Microsoft Teams：Start, stop, and download live transcripts](https://support.microsoft.com/en-us/teams/meetings/start-stop-and-download-live-transcripts-in-microsoft-teams-meetings)
- [Google Meet：Record a video meeting](https://support.google.com/meet/answer/9308681)
- [Google Meet：Use Transcripts](https://support.google.com/meet/answer/12849897)
- [YouTube：Add subtitles & captions](https://support.google.com/youtube/answer/2734796)
- [YouTube：Supported subtitle and closed caption files](https://support.google.com/youtube/answer/2734698)

</main>
