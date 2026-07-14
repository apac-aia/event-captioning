from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "ai-captioning-ballroom-solution.md"
OUTPUT = ROOT / "ai-captioning-ballroom-solution.enhanced.md"


SECTIONS = [
    (
        "## 1. 一句話結論",
        "sec-conclusion",
        "先確認混音器乾淨人聲訊號，再比較人工智慧工具；沒有乾淨聲音，後面都是猜。",
    ),
    (
        "## 2. 這份報告怎麼讀",
        "sec-how-to-read",
        "依角色讀不同段落：決策者看結論，執行者看方案與操作流程，對外溝通看白話版本。",
    ),
    (
        "## 3. ADALS 要解決的不是一件事，而是六塊積木",
        "sec-six-blocks",
        "把現場字幕拆成麥克風、乾淨聲音、字幕電腦、工具、觀眾入口、人力修正六塊，才容易放大或縮小。",
    ),
    (
        "## 4. 為什麼「混音器乾淨人聲訊號」是主角",
        "sec-clean-訊號",
        "人工智慧不是在聽現場空氣，而是在吃一條音訊；這條音訊越乾淨，字幕越穩。",
    ),
    (
        "## 5. 不同規模怎麼小型化",
        "sec-scale",
        "同一套架構可從 20 人小測試放大到 500 人正式會議，差別在每塊積木的厚度。",
    ),
    (
        "## 6. 有人需要字幕／手語才能參加、一般翻譯字幕、實驗功能，要分開說",
        "sec-access-levels",
        "一般翻譯字幕很好用，但有人需要字幕或手語才能參加時，要依對方需求補人工字幕、同步聽打或手語。",
    ),
    (
        "## 7. 現場音訊怎麼接：用圖看就好",
        "sec-audio-路由",
        "所有講話都要進麥克風，再從混音器送給字幕電腦；問答麥克風是最容易漏掉的洞。",
    ),
    (
        "## 8. 工具比較：先看適不適合現場，不要只看人工智慧很強",
        "sec-tools",
        "比較工具時先看現場流程、QR 觀眾端、術語表、人工修正與採購難度，而不是只看模型名稱。",
    ),
    (
        "## 9. ADALS 工具短名單",
        "sec-shortlist",
        "第一輪試測建議測 Vurbo.ai、KKCO、EventCAT、Akkadu、UDTalk，並用同一段 ADALS 測試稿比較。",
    ),
    (
        "## 10. 三套可落地方案",
        "sec-packages",
        "低成本試跑、正式建議方案、高穩定低風險 三套方案對應不同人數、風險與預算。",
    ),
    (
        "## 11. 台北場地：公開價格、飯店報價與總成本比較",
        "sec-venues",
        "飯店沒有被排除；把非飯店場地、飯店公開會議專案、需詢價場地和已知報價放在一起看總成本。",
    ),
    (
        "## 12. 可以直接寄給場地 / 影音團隊的問題清單",
        "sec-rfp",
        "這一章可直接複製寄給場地與影音團隊，用來確認現場能否支援字幕音訊與網路需求。",
    ),
    (
        "## 13. 時程檢查清單",
        "sec-timeline",
        "用 60 / 30 / 14 / 7 / 1 天節奏拆工作，避免活動前一天才發現沒有聲音路由。",
    ),
    (
        "## 14. 現場操作流程",
        "sec-現場操作手冊",
        "開場前 90 分鐘的測試、主持提醒、字幕操作員、志工修正和問答麥克風遞送人員都要有固定動作。",
    ),
    (
        "## 15. 壞掉時怎麼救",
        "sec-failures",
        "先判斷是沒聲音、爆音、延遲、Wi-Fi、QR、沒拿麥克風，然後用對應流程救回來。",
    ),
    (
        "## 16. 術語表：這是讓人工智慧少犯傻的字典",
        "sec-術語表",
        "ADALS、a11y、WCAG、ARIA、人名與組織名要先準備，人工智慧才比較不會亂猜。",
    ),
    (
        "## 17. 資料與隱私",
        "sec-隱私",
        "把聲音送進字幕工具就像交給外部打字員，要確認保存、刪除、訓練與資料所在地。",
    ),
    (
        "## 18. 最終建議",
        "sec-recommendation",
        "先試測、台灣優先、EventCAT 備援、Akkadu 低成本備援；有正式無障礙需求就加人工服務。",
    ),
    (
        "## 19. 採購決策表",
        "sec-decision-table",
        "用是 / 否 問題快速判斷現在該解影音、選試跑、上正式方案，還是補專業服務。",
    ),
    (
        "## 20. 附錄：給主持人的提醒詞",
        "sec-host-script",
        "主持人提醒不是禮貌話，而是讓所有發言進麥克風、讓字幕能工作的現場規則。",
    ),
    (
        "## 21. 附錄：測試腳本",
        "sec-test-script",
        "不要只說「測試、測試」；用含 ADALS 術語、英中日韓、人名、座談與問答 的稿子測。",
    ),
    (
        "## 22. 附錄：來源索引怎麼用",
        "sec-source-index",
        "採購前用來源索引重新確認官方功能、價格與條款，因為雲端軟體服務會變。",
    ),
    (
        "## 23. 最後再用一個比喻收尾",
        "sec-closing-metaphor",
        "現場字幕像行李輸送帶；每句話都要先上正確輸送帶，後面才有機會貼對語言標籤。",
    ),
]

FOCUSED_NAV_IDS = {
    "sec-conclusion",
    "sec-clean-訊號",
    "sec-scale",
    "sec-tools",
    "sec-packages",
    "sec-rfp",
    "sec-現場操作手冊",
    "sec-failures",
}


def nav_html() -> str:
    cards = []
    for heading, section_id, highlight in SECTIONS:
        if section_id not in FOCUSED_NAV_IDS:
            continue
        label = heading.removeprefix("## ").strip()
        cards.append(
            f'<a class="chapter-card" href="#{section_id}">'
            f"<strong>{label}</strong>"
            f"<span>{highlight}</span>"
            "</a>"
        )

    return "\n".join(
        [
            '## 0. 版本與章節導覽 {#sec-navigation}',
            "",
            '<div class="version-switch" role="navigation" aria-label="閱讀版本">',
            '<a href="ai-captioning-ballroom-solution.mobile.html">手機版 HTML</a>',
            '<a href="ai-captioning-ballroom-solution.desktop.html">桌面版 HTML</a>',
            '<a href="ai-captioning-ballroom-sources.html">來源索引</a>',
            "</div>",
            "",
            '<div class="section-highlight section-highlight-primary">',
            "<strong>閱讀建議</strong>",
            "<p>手機上先開手機版 HTML；桌面閱讀用桌面版 HTML。需要穩定分享時，先分享整個 HTML 套裝與來源索引，PDF 等定稿後再產生。</p>",
            "</div>",
            "",
            "下方只列最常用的 8 個入口。完整章節在桌面版左側目錄，或用瀏覽器搜尋章節名稱。",
            "",
            '<div class="chapter-guide" aria-label="章節導覽">',
            *cards,
            "</div>",
            "",
            '<div class="page-break"></div>',
        ]
    )


def highlight_html(index: int) -> str:
    _heading, _section_id, highlight = SECTIONS[index]

    return "\n".join(
        [
            '<div class="section-highlight">',
            "<strong>本章重點</strong>",
            f"<p>{highlight}</p>",
            "</div>",
            "",
        ]
    )


def simplify_source_line(line: str) -> str:
    if line.startswith("官方來源："):
        return "來源：供應商官方頁、價格訊號與支援文件已集中整理在來源索引；正文保留判斷，不在每段打斷閱讀。"
    return line


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    section_by_heading = {heading: (idx, section_id) for idx, (heading, section_id, _) in enumerate(SECTIONS)}

    lines = text.splitlines()
    enhanced: list[str] = []
    inserted_nav = False

    for line in lines:
        if line in section_by_heading:
            idx, section_id = section_by_heading[line]
            label = line.removeprefix("## ").strip()
            enhanced.append(f"## {label} {{#{section_id}}}")
            enhanced.append("")
            enhanced.append(highlight_html(idx))
            continue

        line = simplify_source_line(line)
        enhanced.append(line)

        if not inserted_nav and line.startswith("來源索引"):
            enhanced.append("")
            enhanced.append(nav_html())
            inserted_nav = True

    if not inserted_nav:
        raise RuntimeError("Could not find 來源索引 line to insert navigation.")

    OUTPUT.write_text("\n".join(enhanced).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
