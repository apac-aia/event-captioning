# 字幕方案研究資料（餵工具用）

來源：vault `_yorozuya/research/2026-06-25-captioning-gap-research.md`（完整研究與引用）。本檔經 WebFetch 查證；費率與具名窗口採購前仍須個案確認。

## 手語語種選擇框架
手語不是通用語言，全球300種以上手語互不相通（ASL 與 BSL 不同語系、不互通；台灣手語 TSL 與日本手語 JSL 雖約60%詞彙相似仍非同一語言），所以選哪種手語必須看實際與會者組成，活動報名時就應蒐集手語偏好。判斷框架：(1)在地聾人為主，用主辦國在地手語（台灣=TSL、日本=JSL、澳洲=Auslan、新加坡=SgSL）；(2)國際混合觀眾為主，以 International Sign（IS）為主、在地手語為副；(3)遠端/直播觀眾國籍無法確認，IS（線上廣播）＋在地手語（現場）雙軌；(4)純英語系國際活動在 APAC 舉辦、聾人背景不明，先排 IS＋Auslan 雙軌，再依報名資料補 TSL/JSL/SgSL。關鍵供給限制：APAC 可確認的 WFD-WASLI 認證 IS 口譯員極少（日本1名、澳洲3名），IS 口譯必須提早預訂並查驗認證效期（5年）；在地口譯員通常只受訓本國手語、不具 IS 能力，聘用前要先確認資歷。此框架由 WASLI、WFD、CNCF 三方最佳實踐一致。

## 平台內建字幕
| 平台 | 即時字幕 | 翻譯字幕 | 費用 | 繁中 | 來源 |
|---|---|---|---|---|---|
| Zoom — 即時字幕 (Live Captions / Automated Captions) | 有 | 是。Translated Captions 功能可讓每位參與者各自選擇閱讀語言（ | 翻譯字幕需以下之一：(1) Zoom Workplace Business Plus / Enterprise Esse | 即時字幕辨識語言：46種（含繁體中文、簡體中文、粵語、英文、 | <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059081> |
| Zoom — Translated Captions 加購方案 | 有 | 是 | USD $5/用戶/月（加購）；Business Plus 以上方案內含。 | 繁體中文、簡體中文、英文、日文、韓文、阿拉伯文、孟加拉文、粵 | <https://www.zoom.com/en/blog/translated-captions/> |
| Microsoft Teams — 即時字幕 (Live Captions) | 有 | 是。Live Translated Captions 讓每位參與者選擇自己的閱讀 | 基本即時字幕（無翻譯）：包含在所有 Microsoft 365 商業方案，免費可用。翻譯字幕（Live Translat | 即時字幕辨識：50+ 語言，含繁體中文（台灣）、繁體中文（香 | <https://support.microsoft.com/en-us/teams/meetings/use-live-captions-in-microsoft-teams-meetings> |
| Microsoft Teams Premium — 翻譯字幕 & Interpreter Agent | 有 | 是 | Teams Premium USD $10/用戶/月，需疊加在現有 Microsoft 365 授權。主辦人有 Prem | 翻譯字幕約 100 語言。Interpreter Agent | <https://learn.microsoft.com/en-us/microsoftteams/meeting-transcription-captions> |
| Google Meet — 即時字幕 (Live Captions) | 有 | 是（文字翻譯字幕）。每位參與者可各自選擇閱讀語言，從說話語言即時翻譯為指定語言的 | 基本即時字幕：包含在所有付費 Google Workspace 方案及個人帳號（免費）。翻譯字幕：需 Business  | 即時字幕辨識：103 語言（多數仍為 Beta 版），含英文 | <https://support.google.com/meet/answer/10964115?hl=en&co=GENIE.Platform%3DDesktop> |

## 國際平台
| 名稱 | 類型 | 語言／繁中 | 報價 | 來源 |
|---|---|---|---|---|
| Interprefy | AI字幕 + 即時口譯平台(RSI + AI語音翻譯混合)／ | AI字幕支援 80+ 語言、6,000+ 語言組合;繁中:官方宣稱支援中文,但官方文件未明確列出繁/ | 需報價(彈性按使用量計費,可選時計/日計/年訂制度);第三方估算:活動平台費 $ | <https://www.interprefy.com/> |
| KUDO | 即時口譯平台(人工 RSI + AI語音翻譯混合)／ | 人工口譯 200 語言(含手語);AI 字幕/音訊 77 語言;Interpreter Market | 按量付費(Pay As You Go)適合單次活動;年度方案依使用時數、語言組合 | <https://kudo.ai/> |
| Verbit | AI字幕 + 人工同步聽打 CART(混合)／ | 28+ 語言(部分資料標 30+ 語言);繁中:有 Mandarin(Traditional)支援的 | Self-Service 方案 $29 USD/月(含無限場次、字幕、翻譯);E | <https://verbit.ai/> |
| Otter.ai | AI字幕(自動語音轉錄,會議整合為主)／ | 英文、法文、西班牙文、德文、日文、中文(簡體);繁中:明確不支援,僅簡體中文;計畫未來擴充但無確定時 | Pro $8.33 USD/月(年繳)或 $16.99/月;Business $ | <https://otter.ai/> |
| Wordly | AI字幕 + 即時音訊翻譯(純 AI,無人工口譯)／ | 50+ 語言、3,000+ 語言對;繁中:官方有「Chinese (Traditional)」專頁, | 起價 $75 USD/小時(公開資訊);方案分 Starter(10hr)、Pr | <https://www.wordly.ai/> |
| Interactio | 即時口譯平台(RSI + AI翻譯混合)／ | AI 語音翻譯 65+ 語言;人工口譯語言選項無上限;繁中:未查到明確繁中支援聲明 | 訂閱制:Lite $125/月、Premium $225/月、Leader $3 | <https://www.interactio.com/> |
| SyncWords | AI字幕 + 人工字幕(廣播/直播/活動)／ | AI 字幕 40+ 語言、翻譯 100+ 語言;人工字幕英文、法文、西班牙文、葡萄牙文為主;繁中:未 | 人工轉錄:標準 $1.95/分鐘、快件 $3.45/分鐘;自動字幕 $0.50/ | <https://www.syncwords.com/> |
| InterScribe | AI字幕 + 即時翻譯平台(純 AI,活動/會議/教育用)／ | 100+ 語言即時字幕及翻譯;繁中:官方有「Chinese (Traditional) ZH-TW」 | 月訂制:Launch $349/月(10hr/月,500人)、Engage $4 | <https://interscribe.io/> |
| Boostlingo | AI字幕 + 即時口譯平台(語言服務商整合型)／ | AI 字幕 130+ 語言;人工口譯 300+ 語言;繁中:語言列表頁提到 CJK 支援但未獨立確認 | 需報價(官方無公開固定價格) | <https://boostlingo.com/> |

## 台灣同步聽打（CART）
**身心障礙者權益保障法第61條**
- 區域／費用：台灣（中央法規）｜無費用規定（各地方政府訂定）
- 聯絡／備註：最新修正日期：民國114年8月1日。條文規定手語翻譯員需具技術士資格（法施行第五年起），同步聽打員資格由地方自訂。來源：全國法規資料庫
- 來源：<https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0050046>

**社團法人中華民國聽障人協會（受託承辦台北市聽語障溝通服務）**
- 區域／費用：台灣（台北市）｜免費（台北市政府補助）；外縣市使用者請洽詢
- 聯絡／備註：申請方式：電話、簡訊、傳真、Email、通訊軟體或線上申辦系統，服務前3日申請（緊急不限）。聽打服務時間08:00-22:00。免付費電話：0800-365-224；手機/簡訊：0963-047-723；傳真：0800-365-624。協會地址：台北市士林區承德路四段58巷10弄6號1樓，電話02-28852120。來源：台北市社會局官網
- 來源：<https://dosw.gov.taipei/cp.aspx?n=A1FBE0253EA9B6E1>

**中華民國聾人協會（受託承辦新北市手語翻譯暨同步聽打服務）**
- 區域／費用：台灣（新北市）｜免費（新北市政府補助）
- 聯絡／備註：申請方式：填寫申請表後傳真至0800-365-524或寄至ntcst@nad.org.tw；服務前5日申請。個人需持身心障礙證明（聽語障類別）；機關單位可直接申請。電話：02-2552-3082；Email：deaf@nad.org.tw。來源：新北市政府線上申辦、衛福部輔具資源入口網
- 來源：<https://www.nad.org.tw/storage/templates/ntpc_sl_cart_service.html>

**社團法人台中市聾人協會（受託承辦台中市手語翻譯暨同步聽打服務）**
- 區域／費用：台灣（台中市）｜免費
- 聯絡／備註：申請需服務前3日填寫申請表。預約專線：0965-560-525、04-2201-0080；傳真：04-2201-0060；承辦人：林小姐，04-2228-9111分機37349。來源：台中市政府社會局官網
- 來源：<https://www.society.taichung.gov.tw/461762/post>

**社團法人高雄市聲暉協會（受託承辦高雄市同步聽打服務）**
- 區域／費用：台灣（高雄市）｜免費（高雄市民）；外縣市收費請洽07-2315626
- 聯絡／備註：申請需服務前3日提出；個人申請需持身心障礙證明；機關/非營利單位可直接申請。電話：07-2315626。來源：高雄師大特殊教育中心轉知公文、高雄市社會局
- 來源：<https://ksped.nknu.edu.tw/resource/UploadFile/News/2020221143534/%E8%81%BD%E6%89%93%E6%9C%8D%E5%8B%99%E7%94%B3%E8%AB%8B%E9%A0%88%E7%9F%A5.pdf>

**社團法人屏東縣聲暉聽障協進會（受託承辦屏東縣同步聽打服務）**
- 區域／費用：台灣（屏東縣）｜免費；無服務時數與次數之限制
- 聯絡／備註：申請方式：電話、簡訊、Email、傳真、郵寄、視訊或親洽；服務前5日申請；個人需檢附身心障礙證明影本，團體需檢附立案證書影本。電話：08-7372174；簡訊：0979-812-665；Email：a7354930@yahoo.com.tw；地址：屏東市建豐路180巷35號（屏東縣身心障礙福利服務中心5樓）。來源：屏東縣政府社會處官網
- 來源：<https://www.pthg.gov.tw/planjdp/cp.aspx?n=920104B7056B7226&s=CFD7CF1F424C8E79>

**社團法人桃園市聲暉協進會（受託承辦桃園市同步聽打服務）**
- 區域／費用：台灣（桃園市）｜免費
- 聯絡／備註：電話：03-284-1540、0966-562-631；傳真：03-457-7709；Email：sound.t28@msa.hinet.net；LINE ID：0966-562-631；地址：桃園市平鎮區成德路8巷22號。來源：桃園市政府社會局官網
- 來源：<https://sab.tycg.gov.tw/home.jsp?aplistdn=ou%3Ddata%2Cou%3Dhinder%2Cou%3Dchsocial%2Cou%3Dap_root%2Co%3Dtycg%2Cc%3Dtw&dataserno=202002260001&id=30553&mcustomize=onemessages_view.jsp&parentpath=0%2C30484%2C30490&toolsflag=Y>

**新竹市聲暉協會（受託承辦新竹市同步聽打服務）**
- 區域／費用：台灣（新竹市）｜免費（非營利免費活動）
- 聯絡／備註：電話：03-561-0268；傳真：03-561-0469；Email：hc035@hotmail.com；地址：300新竹市東南街142巷28號。來源：新竹市聲暉協會官網
- 來源：<https://www.brightsound.url.tw/index.html>

**TASLI 台灣手語翻譯協會（全台同步聽打服務資訊整合）**
- 區域／費用：台灣（全台）｜政府委辦服務免費（條件內）；自費翻譯媒合另議
- 聯絡／備註：電話：0936-463-953（優先Email）；Email：tasli.tw@gmail.com；地址：台北市松山區民族東路680號6樓。衛福部補助標準修訂（甲乙丙類改為一二三類）已於近期調整。來源：TASLI官網
- 來源：<https://taslifamily.org/?page_id=598>

**衛生福利部社會及家庭署「各地方政府手語翻譯及同步聽打服務申辦資訊」（2026年4月版）**
- 區域／費用：台灣（中央主管機關）｜各縣市政府委辦服務免費（條件內）
- 聯絡／備註：最快路徑：直接至各縣市社會局/處身心障礙福利科查詢，或聯繫TASLI取得最新縣市窗口清單。來源：銘傳大學前程規劃處公告（轉知版本）
- 來源：<https://cpc.mcu.edu.tw/2026/05/19/%E8%BD%89%E7%9F%A5%E8%A1%9B%E7%94%9F%E7%A6%8F%E5%88%A9%E9%83%A8%E7%A4%BE%E6%9C%83%E5%8F%8A%E5%AE%B6%E5%BA%AD%E7%BD%B2%E5%BD%99%E6%95%B4%E4%B9%8B%E3%80%8C%E5%90%84%E5%9C%B0%E6%96%B9%E6%94%BF%E5%BA%9C/>

**中華民國聾人協會（全台同步聽打員培訓主辦機構）**
- 區域／費用：台灣（全台，總部台北）｜培訓班需報名（部分縣市免費，部分收押金如500元）；服務申請依各縣市規定
- 聯絡／備註：招募資格：18歲以上、高中職以上、中文打字60字/分鐘以上。電話：02-2552-3082；Email：deaf@nad.org.tw；地址：台北市大同區太原路197號2樓。來源：中華民國聾人協會官網
- 來源：<https://www.nad.org.tw/archives/2380>

**速錄台灣（sulutw）**
- 區域／費用：台灣｜需報價（網站提供聯絡表單，無公開費率）
- 聯絡／備註：服務項目：會議速記、法庭紀錄、詢問記錄、採訪記錄、口述記錄、錄音轉譯。來源：速錄台灣官網
- 來源：<https://sulutw.weebly.com/>

**雃思工坊（Arsz）**
- 區域／費用：台灣（台中市）｜學術訪談17元/分鐘；校安訪談/會議20元/分鐘；法律案件50元/分鐘；大量委案可議價（幣別：新台幣）
- 聯絡／備註：電話：04-22293452；地址：台中市民族路192號。服務含逐字稿製作、字幕製作、翻譯服務。來源：雃思工坊官網
- 來源：<https://arsz.idv.tw/>

**PRO360達人網（聽打員媒合平台）**
- 區域／費用：台灣（線上媒合平台）｜500-1000元/半小時（新台幣）；錄音轉譯起價500元/30分鐘；現場即時服務多為事後交件
- 聯絡／備註：平台免費建立專家檔案，接案0%佣金。來源：PRO360達人網
- 來源：<https://www.pro360.com.tw/category/listen_and_keyin>


## 台灣手語翻譯
**社團法人台灣手語翻譯協會 (TASLI)**
- 區域／費用：台灣（台北市松山區）｜1. 政府補助額度內免費（北市身障者每月4小時、其他身障者每月2小時）。2. 企業/商業自費：比照社會局補助標準收費，具體金額未公開，需 Email 詢問（tasli.tw@gmail.com）。3. 私人婚喪喜慶等長時間需求可媒合自費翻譯
- 聯絡／備註：聯絡：tasli.tw@gmail.com / 02-6605-0455。地址：台北市105松山區民族東路680號6樓。
- 來源：<https://taslifamily.org/>

**TASLI 譯聯網（視訊手語服務）**
- 區域／費用：台灣（台北市政府社會局補助，TASLI 主辦）｜北市身障者：每月4小時免費；其他身障者：每月2小時免費；同一活動累計最高6小時。企業單位自費比照社會局補助標準（具體金額需洽詢）
- 聯絡／備註：服務電話 02-6605-0455 / 0928-338-235。企業申請可基於社會責任使用，具體費率需個案確認。
- 來源：<https://taslifamily.org/?page_id=7458>

**衛生福利部社會及家庭署 手語視訊轉譯中心（VRS）**
- 區域／費用：台灣（中央政府，衛福部主辦）｜免費（對聽語障者，由政府負擔），非屬替代電話的活動現場翻譯不在本服務範圍
- 聯絡／備註：iOS App: https://apps.apple.com/tw/app/%E6%89%8B%E8%AA%9E%E8%A6%96%E8%A8%8A%E8%BD%89%E8%AD%AF/id6472778865；Android: https://play.google.com/store/apps/details?id=vrs.sfaa
- 來源：<https://vrs.sfaa.gov.tw/>

**社團法人中華民國聽障人協會（CNAD）— 台北市手語翻譯暨聽打服務**
- 區域／費用：台灣（台北市）｜台北市設籍身障者：每月30小時補助（手語翻譯+聽打合計）；非設籍者10小時。超額自費，預算詳情需向社會局申請。
- 聯絡／備註：CNAD 網站有部分頁面出現 404 錯誤，服務細節建議直接電話確認。
- 來源：<http://www.cnad.org.tw/>

**社團法人中華民國聾人協會（NAD）— 新北市手語翻譯暨同步聽打**
- 區域／費用：台灣（新北市）｜符合資格者免費（需設籍新北市並持身障證明）；申請至少5個工作天前提出
- 聯絡／備註：NAD 同時承辦宜蘭縣、新竹市等多縣市服務，詳見其官網服務專區。
- 來源：<https://www.nad.org.tw/%E6%9C%8D%E5%8B%99%E5%B0%88%E5%8D%80/ntcst>

**社團法人台中市聾人協會 — 台中市手語翻譯暨同步聽打**
- 區域／費用：台灣（台中市）｜符合資格者免費；商業利益活動需自費（金額需洽詢）。申請至少提前3天（一般申請）
- 聯絡／備註：主管機關為台中市政府社會局：https://www.society.taichung.gov.tw/461762/post
- 來源：<http://www.taftd.org.tw/OnePage.aspx?tid=120>

**高雄市手語翻譯服務（平安社會福利慈善事業基金會承辦）**
- 區域／費用：台灣（高雄市）｜符合資格者免費（補助範圍內）；涉商業利益需自費。具體金額需洽詢。
- 聯絡／備註：地址：高雄市三民區中華二路250號4樓。
- 來源：<https://socbu.kcg.gov.tw/index.php?prog=2&b_id=5&m_id=213&s_id=413>

**社團法人台南市聲暉協進會 — 台南市手語翻譯服務**
- 區域／費用：台灣（台南市）｜符合資格者免費；涉私人商業利益需自費（金額需洽詢）
- 聯絡／備註：申訴聯絡社會局：06-2991111#8652。
- 來源：<https://sab.tainan.gov.tw/cl.aspx?n=26870>

**社團法人桃園市聾啞福利協進會 — 桃園市手語翻譯服務**
- 區域／費用：台灣（桃園市）｜符合資格者免費；不受理私人商業利益活動。就業相關手語翻譯可洽桃園市勞動局
- 聯絡／備註：地址：桃園市八德區介壽路二段901巷49弄91號。
- 來源：<https://sab.tycg.gov.tw/News_Content.aspx?n=7325&s=1001173>

**基隆市社會處 身心障礙福利科 — 基隆市手語翻譯暨同步聽打服務**
- 區域／費用：台灣（基隆市）｜符合資格者免費；需至少提前3天提出申請
- 聯絡／備註：服務限公共參與、就醫、就業等事務，私人商業利益場合不適用。
- 來源：<https://www.klcg.gov.tw/tw/social/2803.html>

**TASLI 全台手語翻譯窗口彙整（衛福部社家署委托資訊）**
- 區域／費用：台灣（全國）｜各縣市服務條件不同，通常免費限身障者在特定場合使用；需個別洽詢各縣市窗口
- 聯絡／備註：TASLI 另提供全台自費媒合，Email：tasli.tw@gmail.com。
- 來源：<https://taslifamily.org/?page_id=364>


## 手語語種與國際供應商
| 手語語種 | 何時用 | APAC 適配 |
|---|---|---|
| International Sign (IS) | 國際混合觀眾的活動主語言;聯合國、WFD、Deaflympics 等跨國場合標準配備;直播或遠端觀眾國籍不明時的最廣覆蓋選項 | APAC 首選跨國溝通語言。2025 年 WASLI 亞洲區大會(馬來西亞吉隆坡)同步提供 IS、英語口語、馬來西亞手語三軌,印證 IS 為 APAC 國際活動主流選擇。缺點:APAC 地區 WFD-WASLI 認證 IS 口譯員極少(日本 |
| Auslan(澳洲手語) | 澳洲或紐西蘭為主辦地,或聾人與會者多為澳洲/紐西蘭籍時 | APAC 英語系國家首選在地手語。澳洲有最完整的 APAC 認證 IS 口譯員群(3 名),Expression Australia、Sign Language Australia、Deaf Connect 等機構提供 NAATI Conf |
| 台灣手語 TSL | 台灣本地舉辦的活動,或聾人與會者多為台灣籍時 | 台灣有政府支持的 TSL 口譯體系及 13 個全國聾人協會,可透過當地聾人協會媒合 TSL 口譯員。與 JSL 有 60% 詞彙相似度但非同一語言。不建議用於跨國活動主語言。 |
| 日本手語 JSL | 日本本地舉辦的活動,或聾人與會者多為日本籍時 | 由日本手語口譯員協會(JASLI)管理認證考試 SLICE,有 2,384 名會員。活動可透過 JASLI 或日本聾人協會媒合。不具備跨國活動覆蓋能力,且與 IS 無直接互通。 |
| 新加坡手語 SgSL | 新加坡本地舉辦的活動,或聾人與會者多為新加坡籍時 | 由新加坡聾人協會(SADeaf)提供口譯服務,支援 SgSL、PSE、SEE。未提供 IS。主要服務新加坡本地機構、政府、法院等。費率 2025 年 10 月起調整,需提前至少 7 個工作日預約。 |
| ASL(美式手語) | 與會者多為北美聾人(美國/加拿大)時;或活動以英語系北美觀眾為主要遠端受眾時 | ASL 在 APAC 本地聾人社群中不通用。CNCF 建議:北美活動 ASL 為明確首選,但在歐洲或 APAC 國際活動中,ASL 應作為副語言(服務北美遠端參與者),主語言應為 IS 或在地手語。 |
| BSL(英式手語) | 與會者多為英國聾人時;英國境內活動的首選 | BSL 在 APAC 幾乎無在地基礎,APAC 聾人社群不通用。除非確認有大量英國籍聾人與會者,APAC 活動不建議以 BSL 為主語言。BSL 與 ASL 屬不同語系,彼此不通。 |

| 供應商 | 手語 | 模式 | APAC 備註 | 來源 |
|---|---|---|---|---|
| Overseas Interpreting | International Sign(主力)、各國手語、口語 | 線上/現場/混合三種模式皆可 | 明確聲稱與全球 50 國以上合作、特別關注全球南方與亞洲口譯員網絡;持有 WFD-WASLI 認證 IS 口譯員;APAC 活動可服務但據點在西班牙瓦倫西亞,需確認時差與差旅安排 | <https://overseasinterpreting.com/> |
| WASLI IS 認證口譯員名單(日本 / 澳洲) | International Sign | 視個別口譯員而定 | WASLI 公開名單中確認:日本 1 名(川上惠,聾人)、澳洲 3 名(Cave、Levitzke-Gray、Emerson)。可直接聯繫洽談。認證效期 5 年,需確認現行有效性 | <https://wasli.org/sign-language-interpreters/is-accredited-interpreters/> |
| Expression Australia | Auslan(澳洲手語) | 現場/線上皆可 | 澳洲最具規模的聾人服務機構(1884 年創立),提供大型會議 Auslan 口譯;NAATI Conference Level 認證口譯員;提供技術諮詢協助推廣給聾人社群 | <https://www.expression.com.au/services/interpreting-and-captioning/auslan-interpreting-for-conferences-and-events> |
| SADeaf Deaf Access Services(新加坡聾人協會) | 新加坡手語 SgSL、PSE、SEE | 現場為主 | 新加坡本地活動首選;服務政府、學校、法庭、企業;費率 2025 年 10 月更新,需提前 7 個工作日預約 | <https://sadeaf.org.sg/service/interpreting/> |
| JASLI(日本手語口譯員協會) | 日本手語 JSL | 主要為日本境內現場 | 協會本身不直接派遣口譯員(以訓練與認證為主),但可作為查找 SLICE 認證 JSL 口譯員的媒合入口;2,384 名會員 | <https://www.jasli.jp/english.html> |
| Sign Language Australia (SLA) | Auslan | 現場/視需求 | 澳洲 100% 聾人主導的 Auslan 口譯服務,位於阿德萊德;提供口譯員查找功能 | <https://signlanguageaustralia.com/find-an-interpreter/> |
