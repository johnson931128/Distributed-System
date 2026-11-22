# 筆記驗證紀錄

本檔保留分批驗證紀錄：第 1–5 節為 2026-11-19 的 P1–P62 批次；第 6 節起為 2026-11-20 的 P63–P117 批次。舊表的「當次未展開／未 push」是歷史狀態，不能取代後續紀錄。**撰寫完成、本機驗證、線上雙平台驗收是三個不同狀態。**

## 1. 教材與內容核對

| 項目 | 結果與界線 |
| --- | --- |
| PDF 身份與頁數 | 合併講義 270 頁；原文書 685 頁，題名頁 4.03x。版本內部差異與 SHA-256 見 [教材紀錄](reference/README.md) |
| 頁序 | P18／P41／P63 章節封面符合本次範圍；所有十章起點與結尾完成結構核對 |
| 本次教材閱讀 | 已抽取並讀取 P1–P63 文字；P63 僅確認下一章封面 |
| 原圖人工核對 | 已渲染並檢視 P24、P26、P30、P33、P36、P37、P38、P40、P59、P60，確認箭頭方向與數值 |
| 來源差異 | 保留 Week 1／Week 2、Phase 3、P60 原例與補充案例的差別；課程政策保留 P15 暫定性 |
| 不在本次範圍的 PDF 異常 | P145、P205、P207、P208 遺失 XObject resource 警告已記錄；未修復原始教材 |
| 技術條件 | 已對照原始論文補足 FIFO、FLP、持久 Promise／Accepted、Adoption、Raft 日誌新舊與 currentTerm 提交條件 |

## 2. 可執行算例核算

在 Repository 根目錄執行：

```text
python tools/verify-examples.py
```

本次實際輸出：

```text
PASS: P24/P26 timestamps and 225 event-pair causality checks
PASS: P33 conservation; 27 checkpoint combinations; R-Graph; domino trace
PASS: quorum intersections; adoption; Raft freshness and old-term counterexample
All finite example checks passed; this is not a full protocol proof.
```

時鐘比較另以事件祖先集合核對向量關係；checkpoint 組合以逐訊息 send／receive 是否包含核對。共識部分檢查有限 quorum 與選值、選票案例，**不是** 完整協定實作、全訊息排程探索或形式證明。

## 3. Markdown 與 Mermaid 本機驗證

使用 markdown-it 解析 Markdown，並在 headless Microsoft Edge 中載入 Mermaid，實際渲染三篇筆記的圖表。工具套件與預覽圖保存在系統暫存目錄，未加入 Repository。

| 項目 | 結果 |
| --- | --- |
| UTF-8 內容 | 已重新讀取所有 Markdown；沒有 Unicode replacement character 或連續問號損毀。先前 PowerShell 管線造成的問號內容已重建 |
| 三章內容 | Chapter 00／01／02 共 21 題英文單選題，每題包含 A–D 解析 |
| Mermaid | 共 9 圖；全部完成解析與 SVG 渲染，並逐張檢視生成圖 |
| Markdown 表格 | 最終解析 9 份 Markdown，共 43 張表；三章渲染後未發現欄數不一致 |
| 程式碼區塊 | 未發現未關閉 fence；Mermaid 使用 flowchart、sequenceDiagram、stateDiagram-v2 的基本語法 |
| 章節連結 | 16 個本機 Markdown 檔案連結通過存在性檢查；HackMD Note URL 均保持待連結 |
| 公式 | 採 Unicode／行內程式碼的文字表達，如 `q = ⌊N/2⌋ + 1`，無需平台專屬數學渲染 |
| 圖片 URL | 沒有新增 Markdown 圖片；圖片來源／授權檢查不適用。所有技術圖為內嵌原創 Mermaid |
| 桌面預覽 | 1280px 視窗，三篇無頁面水平溢出；沒有 browser pageerror |
| 窄螢幕預覽 | 390px 下 Chapter 00 無水平溢出；Chapter 01／02 的寬表最小寬度約 528／565px，需平台提供水平捲動，仍保留發布後檢查項目 |

這是本機 CommonMark／GFM 相容語法與 Mermaid 預覽，沒有複製 GitHub 或 HackMD 的實際渲染器、CSS 或 Mermaid 版本。窄螢幕表格的水平捲動必須在目標平台另驗，不縮小圖中文字來冒充可讀。

已修正中文術語後接正文時，CommonMark 對粗體結尾標點的解析問題。寬時序圖在手機預覽會隨可用寬度縮放；文字推演與狀態表保留完整內容，發布後仍需確認平台能水平捲動或放大閱讀圖表。

## 4. 外部來源與 Git 保護

正文採用的 Lamport 時鐘、Snapshot、Paxos、Part-Time Parliament、FLP、Netzer–Xu、Raft、原文書作者頁、etcd 與 ZooKeeper 官方連結，已實際讀取；最初 Microsoft Research 的 Part-Time Parliament 路徑回傳 404，已改成作者提供的 PDF。

Dynamo 論文與 Flink 2.1 官方資料另作 Chapter 01 的實際應用補充，明確區分原始協定與產品設計。來源清單與查詢日期列於章末，不使用外部圖片。

提交前檢查 `git diff --check` 與 staged diff；只選取本次筆記、規範、索引與算例程式。使用 `git check-ignore` 確認兩份 `reference/*.pdf` 被忽略；PDF 留在本機，不列入提交。

## 5. 尚未執行的驗收

| 項目 | 狀態 | 待完成條件 |
| --- | --- | --- |
| GitHub 實際文件顯示 | NOT_RUN | 本次尚未 push；發布後檢查表格、Mermaid、文字公式與章節導覽 |
| HackMD 實際 Note 顯示 | NOT_RUN | 尚無 Note URL；從已發布 GitHub 檔案逐篇 Pull，確認兩平台內容一致 |
| 外部圖片／raw URL | 不適用 | 本次沒有圖片資產；未來新增時先提交 GitHub 再驗證顯示 |
| 真實叢集故障注入／效能 | NOT_RUN | 本次為學習筆記與有限算例；未部署 Paxos、Raft、Flink 或 checkpoint 服務 |
| P63 起完整筆記 | 未展開 | 下一次從 ZooKeeper 封面與對應教材重新閱讀 |

此紀錄不代表已完成線上雙平台驗收，也不代表原始協定的所有實作細節均已測試。

## 6. 2026-11-20：Chapter 03／04 的教材與技術核對

新增筆記為 `notes/03-zookeeper.md`（P63–P89）與 `notes/04-peer-to-peer-gossip.md`（P90–P117）。已重新讀取此 55 頁文字，並檢視 P67、P78、P84、P88、P103、P106、P107、P109、P110、P112、P116 的渲染圖。P118 只確認下一章封面，未展開內容。

核對重點包括四投票者的 quorum 基數、ZAB 與交易 2PC 的界線、Session／TCP、標準 Watch 與漏通知競爭、sync 語義限制、Gossip 單輪條件期望與近似、Chord successor／finger、CFS 原始唯讀語義與可變資料的共識延伸。差異逐項列在 [教材紀錄](reference/README.md)。

官方文件以 ZooKeeper 3.9.4 固定版本核對；新增七篇論文已下載至本機 `reference/`，檔頭、題名、頁數、可讀文字與 SHA-256 均已記錄。只引用實際閱讀的相關範圍，不宣稱已重現所有論文實驗與證明。

13 個新章節的唯一外部引用 URL 中，12 個以 Python HTTP GET 成功取得；Microsoft 的 Sybil PDF 對該 HTTP client 回傳 403，但已以 Windows Invoke-WebRequest 成功下載並核對原論文。沒有關閉 TLS 憑證驗證；Cornell 的 PDF 曾在 Python client 遇到憑證鏈問題，改用系統信任憑證的 Windows 下載方式後取得。這些差異不被隱藏為「所有工具皆可讀取」。

## 7. 2026-11-20：有限算例驗證

實際執行：

```text
python tools/verify-coordination-p2p.py
```

輸出：

```text
PASS: quorum count, CAS, 15 lock queues, predecessor races and fencing example
PASS: seven-row Gossip table, exact finite-round expectations, six-node dissemination
PASS: CAN split, area conservation and 400 coordinate ownership checks
PASS: Chord fingers, 384 lookups, wraparound, single join and transferred keys
Finite examples passed; no live cluster, full protocol proof or arbitrary churn test.
```

Gossip 除核對正文數值表，也枚舉 N=2–5 的單輪 partner 選擇，比對有限 N 的條件期望，沒有把隨機試跑的結果當成公式證明。Chord 對六個起點、全部 64 個 keys 驗證靜態 ring 的 owner，另核算 wraparound 與 N15 加入後需移交的 keys 11–15。CAN 用 400 個座標點檢查分裂後唯一 owner 與面積守恆，另測切分邊界。

ZooKeeper 部分驗證的是有限隊列、CAS 與前驅消失的教學交錯；不模擬真實 ZAB、網路、SDK、Session Expiration 或持久化。因此不將「算例通過」稱為分散式鎖實作已驗收。原 `python tools/verify-examples.py` 也已重跑，Chapter 01／02 的既有算例全部通過。

## 8. 2026-11-20：本機渲染與尚未完成的驗收

仍以 markdown-it 與 headless Microsoft Edge／Mermaid 檢查語法與本機預覽；所有新圖是內嵌原創 Mermaid，沒有新增公開 SVG／PNG 或外部圖片。

| 項目 | 本批結果 |
| --- | --- |
| 新增英文單選題 | ZooKeeper 8 題、P2P 9 題，共 17 題；每題均含 A–D 解析 |
| 新增 Mermaid | 9 圖（Chapter 03 四圖、Chapter 04 五圖），全部成功解析、渲染並逐張檢視 |
| 桌面預覽 | 1280px 下兩章無頁面水平溢出，表格欄數一致，沒有 browser pageerror |
| 手機預覽 | 390px 下 ZooKeeper 的部分表格最小寬度約 466px，需水平捲動；P2P 無頁面水平溢出，但寬時序圖仍須確認放大可讀性 |
| 文字與導覽 | UTF-8、fence、圖片 URL 規則與本機連結存在性檢查通過；章首保留標題並直接進正文 |
| GitHub 實際顯示 | 新增兩章 NOT_RUN；Chapter 00–02 曾於前批推送，但不能據此宣稱這次新章節已在線上驗收 |
| HackMD 實際顯示 | NOT_RUN；仍無 Note URL，需從 GitHub 已存在檔案 Pull，禁止空白 Note Push |
| 真實服務／網路故障注入 | NOT_RUN；未啟動 ZooKeeper、CAN、Chord、Gossip 或 Web3 部署 |
| 後續章節 | P118 起未展開；使用者閱讀完成狀態未自動前進 |

公開索引更新與 PDF 存檔分開；所有 `reference/*.pdf` 均留在本機。提交前另檢查 staged paths、diff 與忽略規則，避免將教材與下載論文納入 Git。

## 9. 2026-11-22 教學改版

從 `63deb0e` 的同步版本依 04、03、01、02、00 重構。每篇章末的對照表列出講義頁次、概念與原理、圖解與推演，以及轉往下一個主題的問題。核對合併講義 P1–P117 的文字與 19 張關鍵投影片，並依各章用到的範圍對照第 4 版原文書、MIT 課程及原始論文／官方文件。引文的頁碼均指各自 PDF 的實體頁碼。

| 章節 | 改版前的閱讀阻礙 | 改版後的教學路徑 |
| --- | --- | --- |
| 04，P90–P117 | Overlay 問答重複課文，搜尋、散布與定位混在比較表裡 | 從找同一份映像檔解釋每個 Logical Hop，再經多播、目錄、泛洪到 Gossip、CAN、Chord 與 CFS |
| 03，P63–P89 | 元件、API、名詞連續出現，鎖的規則先於可觀測行為 | 工作節點讀設定、ZAB 提交、版本競爭、成員通知、正常排隊，再看監看競爭、到期和外部寫入 |
| 01，P18–P40 | 先讀時鐘分類與 Snapshot 規格，才知道要找出什麼 | 從轉帳日誌進入因果，並排兩種時鐘的四條訊息，先算 50 元快照，再推導 Marker 規則與回復線 |
| 02，P41–P62 | 角色、狀態與完整規則堆在正常路徑前 | 從最後一席及逾時進入 Paxos 10/A，再解釋合法選值；Raft 先看任期 4、index 8，再看選舉限制與五節點反例 |
| 00，P1–P17 | 設計原理集中在抽象比較表，後續章節之間缺少問題銜接 | 用庫存 1→0 和 r1 重送建立提交、故障與去重的直覺，再連到各章機制 |

- 本機 Markdown／渲染通過。以 markdown-it 檢查 11 份 Markdown、34 個相對連結、51 張表格及圍欄。以 headless Microsoft Edge 渲染五章的 22 張 Mermaid 圖。在 1280 px 與 390 px 預覽無頁面水平溢出，長程式碼與文字圖可在各自區塊捲動。公式使用純文字或程式碼，並由算例程式核算。24 題英文單選均有 A–D 選項與逐項解析。
- `python tools/verify-examples.py` 與 `python tools/verify-coordination-p2p.py` 均通過。涵蓋時間戳、快照守恆、檢查點組合、多數相交、提案採用、Raft 新舊日誌、ZooKeeper 排隊競爭、Gossip 機率、CAN 區域及 Chord 路由。測試範圍是有限算例。
- GitHub 與 HackMD 的改版畫面均為 `NOT_RUN`。本次只提交本機版本。所有圖以內嵌 Mermaid 或文字呈現，沒有需要遠端載入的 SVG、PNG 或外部圖片。真實叢集部署、故障注入與效能量測同為 `NOT_RUN`。
- 確認本機教材及 15 份論文 PDF 均受忽略規則保護。P118 起維持待整理。
