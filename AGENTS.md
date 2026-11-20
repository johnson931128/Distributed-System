# AGENTS.md — Distributed Systems 學習筆記專案規範

> Repository: `johnson931128/Distributed-System`  
> Language: 繁體中文（zh-TW），技術名詞保留英文；英文術語首次出現時附中文說明。  
> Main objective: 將國立成功大學 2026 Fall Distributed Systems 課程投影片，擴充成可供長期複習、理解原理、推演演算法與比較系統設計的技術筆記。  
> Target readers: 已具備作業系統、演算法、計算機網路及程式開發基礎的資訊／工程學生。  
> Current progress: 使用者已確認 **P1–P62 已學習，P63 為待閱讀起點**；筆記已整理至 **P117**，Chapter 03／04 待使用者閱讀。下一個整理單元為 P118，未自動展開。

## 0. Agent 工作方式（必須遵守）

1. **先讀本檔，再檢查 Repository 既有檔案。** 修改既有筆記前先閱讀全文，避免覆寫人工編修與 HackMD 同步內容。
2. **先核對教材，再撰寫。** 不得只憑檔名、記憶或網路摘要，假裝已讀過教授的 PDF。沒有教材時應在輸出或進度回報明確標示缺少來源；不可杜撰投影片原文、頁碼或例題。
3. **課程教材決定章節與教學範圍；論文與官方文件負責補充實作、推導、架構及技術細節。** 補充內容不可冒充教授投影片原文。
4. **按章節逐步產出，不要一次用大量空泛文字填滿整份課程。** 本階段優先完成 `notes/00-course-introduction.md`、`notes/01-logical-clocks-checkpointing.md`、`notes/02-fault-tolerance-paxos-raft.md`。直到有明確指令，再開展 ZooKeeper 與後續章節。
5. **主要產物為 Markdown。** 使用 GitHub 與 HackMD 都能正常呈現的 CommonMark／GitHub Flavored Markdown；圖表優先 Mermaid、表格和文字序列圖。禁止依賴僅限某一平台的私有語法。
6. **提供可檢驗的例子，不能只羅列定義。** 對每個重要演算法，說明前提、角色、狀態、消息、完整步驟、成功／失敗案例，以及為何正確。
7. **改動前檢查 Git 狀態。** 不改動無關檔案、不強制推送、不任意刪除筆記。新增或重構多份筆記時先規劃章節和預期檔案；以小而可審查的 commit 提交。
8. **結束時回報**：修改檔案、對應 PDF 頁碼、補充來源、查核項目、尚待確認／尚未完成之處。未實際執行的命令或驗證不可宣稱成功。

## 1. 權威資料與引用規則

### 1.1 課程第一手來源（最高優先權）

- 課程：**Distributed Systems — Fall 2026**，National Cheng Kung University，Prof. Hung-Chang Hsiao（蕭宏章）。
- 主要教材：`reference/整包.pdf`，已核對為 270 頁合併講義；P18、P41、P63 分別為 Logical Clocks、Fault Tolerance、ZooKeeper 封面。
- 原文書：`reference/Distributed_Systems_4.pdf`，685 頁；van Steen 與 Tanenbaum，*Distributed Systems*，4th edition，題名頁 Version 4.03x（February 2025）。原文書實體頁碼須標為「原文書 PDF P…」。版本內部差異見 `reference/README.md`。
- 課程簡介直接使用合併講義 P1–P17；目前未提供獨立 `Intro_Slides.pdf`。
- 若 PDF 尚未放入 Repository，Agent 應先檢查使用者提供的可讀檔案與工作環境；取得明確原始檔後再做依據投影片的整理。
- **公開 Repo 不應直接加入未確認可再散布的 PDF。** 在 `.gitignore` 中忽略 `reference/*.pdf`，並保留 `references/private/` 的舊路徑保護；原始教材僅留本機。
- **頁碼一律使用重排後合併 PDF 的實體頁碼 P1–P270（1-based），不是原始合併檔或各投影片底部的 deck page。**

### 1.2 引用格式

每個主要小節的講義依據應標示為：

> 課程依據：Distributed Systems（NCKU, Fall 2026），P52–P54。  
> 延伸參考：Leslie Lamport, *Paxos Made Simple*（附可用 URL）。

- 引用時指出實際頁碼、文獻標題和連結；不得虛構 DOI、URL、引文或版號。
- **來源層級**必須清楚：`[課程講義]`、`[原始論文／官方文件]`、`[教學補充／推導]`、`[待確認]`。
- 教授投影片是課程考點的依據；若教材有簡化、易混淆說法，先忠實記錄課堂表述，再另外標明「技術補充／更精確的說法」，不得暗中替換。
- 使用網頁來源前優先選論文作者頁面、學術出版頁面、官方文件和實際專案文件。會隨版本變動的行為應註明版本或查詢日期。
- 不大量逐字複製投影片、論文或網站內容；以自行整理的解釋、例子與原創圖為主。

### 1.3 經核對的外部參考資料

**基礎理論、Logical Clocks、Checkpointing：**

- Leslie Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System*：https://lamport.azurewebsites.net/pubs/time-clocks.pdf
- K. Mani Chandy and Leslie Lamport, *Distributed Snapshots: Determining Global States of Distributed Systems*：https://lamport.azurewebsites.net/pubs/chandy.pdf
- MIT 6.5840 Distributed Systems 課程與閱讀資料：https://pdos.csail.mit.edu/6.824/

**Fault Tolerance、Consensus、Paxos、Raft：**

- Leslie Lamport, *Paxos Made Simple*（作者文獻清單）：https://lamport.azurewebsites.net/pubs/pubs.html
- Leslie Lamport, *The Paxos Algorithm*：https://lamport.azurewebsites.net/tla/paxos-algorithm.html
- Diego Ongaro and John Ousterhout, *In Search of an Understandable Consensus Algorithm*：https://raft.github.io/raft.pdf
- Raft 官方教學與互動資源：https://raft.github.io/

**後續章節的官方文件（只在對應章節實際撰寫時引用）：**

- Apache ZooKeeper Programmer's Guide：https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html
- Apache HBase Reference Guide：https://hbase.apache.org/docs/
- Apache Hadoop — HDFS Architecture：https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
- Apache Kafka Documentation：https://kafka.apache.org/documentation/
- Apache Spark Documentation：https://spark.apache.org/docs/latest/
- etcd Documentation：https://etcd.io/docs/

若連結失效，先查找官方替代頁面並記錄實際使用之來源；不可直接聲稱已查核。

## 2. 章節與檔案架構（以 270 頁重排 PDF 為準）

| 順序 | 投影片範圍 | 講義章節 | 筆記路徑 | 狀態 |
| --- | --- | --- | --- | --- |
| 00 | P1–P17 | Course Introduction | `notes/00-course-introduction.md` | 已學習，已撰寫 |
| 01 | P18–P40 | Logical Clocks, Global States, & Checkpointing | `notes/01-logical-clocks-checkpointing.md` | 已學習，已撰寫 |
| 02 | P41–P62 | Fault Tolerance & Paxos Consensus Algorithm（含 Multi-Paxos、Raft） | `notes/02-fault-tolerance-paxos-raft.md` | 已學習，已撰寫 |
| 03 | P63–P89 | Distributed Coordination Services (ZooKeeper) | `notes/03-zookeeper.md` | 已整理，待閱讀 |
| 04 | P90–P117 | Peer-to-Peer Computing (Overlay Networks) | `notes/04-peer-to-peer-gossip.md` | 已整理，待閱讀 |
| 05 | P118–P155 | Data Consistency, Replication & Distributed Transactions | `notes/05-consistency-replication-transactions.md` | 待學習 |
| 06 | P156–P182 | LevelDB and HBase: Distributed Storage Engines | `notes/06-leveldb-hbase.md` | 待學習 |
| 07 | P183–P210 | Distributed Storage and Resource Management（HDFS、MapReduce、YARN、Spark） | `notes/07-hdfs-mapreduce-yarn-spark.md` | 待學習 |
| 08 | P211–P238 | Distributed Data Streaming Architectures（Kafka、Streams） | `notes/08-kafka-stream-processing.md` | 待學習 |
| 09 | P239–P270 | Blockchain Foundations | `notes/09-blockchain-foundations.md` | 待學習 |

補充檔案：

```text
Distributed-System/
├── AGENTS.md
├── README.md                        # GitHub 入口、章節導覽、進度
├── notes/
│   ├── README.md                    # 集中教材資訊、進度與導覽
│   ├── 00-course-introduction.md
│   ├── 01-logical-clocks-checkpointing.md
│   ├── 02-fault-tolerance-paxos-raft.md
│   └── ...                         # 後續依上表逐章新增
├── assets/
│   └── diagrams/                   # 必要時存放自製 SVG／PNG；優先內嵌 Mermaid
└── reference/
    ├── 整包.pdf                     # 本地講義；不提交
    ├── Distributed_Systems_4.pdf     # 本地原文書；不提交
    └── README.md                    # 教材核對紀錄
```

- `README.md` 應提供章節名稱、投影片範圍、學習進度、GitHub 相對路徑、對應 HackMD URL（若已知）；未知的 HackMD URL 寫 `待連結`，不可編造。
- 章節筆記每一份對應一個 `.md` 檔案，方便 HackMD **逐篇**連結 GitHub，避免將所有課程內容塞入一份巨大文件。
- 章節內可有多個 `##`／`###`，不要以一頁投影片產生一個檔案。
- 不要自動建立一堆只有標題的未學習章節；可先在 README 列出未來規劃。

## 3. 筆記寫作規則

### 3.1 語言和風格

- 使用精確、自然的繁體中文，保留關鍵英文術語，如 `Happens-before`、`Vector Clock`、`Majority Quorum`、`Prepare`、`Promise`、`Log Replication`。
- 首次出現的名詞統一格式：**邏輯時鐘（Logical Clock）**。同篇後續使用一致命名。
- 技術文章要像高品質教科書／工程筆記，而不是講義的簡短摘要或 AI 口語聊天。
- 不要出現空泛的「非常重要」「顯而易見」「這裡值得注意的是」等填充詞；每個結論都應說明條件、原因或反例。
- 禁止以泛泛的「系統更有效率」代替技術理由；須指出減少了什麼 RPC、網路往返、I/O、磁碟同步或協調成本。
- 範例符號、公式、訊息格式保持前後一致；每個變數首次出現要定義。
- 不將個人記憶、先前聊天或無來源的細節寫成教授講義內容。

### 3.2 每章建議結構

```markdown
# Chapter NN — 中文章名（English Title）

## 本章要解決什麼問題？
## 核心概念與必要前提
## 系統架構、角色與資料流
## 演算法／協定流程（逐步推演）
## 完整案例（正常路徑）
## 故障、競爭、邊界條件與恢復
## 與相近技術比較（表格）
## 正確性、限制與效能分析
## 常見誤解與考試陷阱
## 重點速查（精簡）
## 練習題（含推理與答案）
## 參考資料與投影片對應
```

此為參考骨架，應依章節實質內容調整，不得為湊版面填寫不相干段落。章首教材與狀態資訊集中至 `notes/README.md`；具體引用放在各主要小節。**完整的推演與解釋放在前面，速查表放在後面。**

### 3.3 深度標準（不可省略）

1. **Why**：問題為何存在？若沒有這項機制會發生什麼故障或矛盾？
2. **What**：精確定義、前提假設、狀態變數與不變量。
3. **Who**：節點角色、責任分工、哪些動作可同時發生。
4. **How**：依時間順序展示訊息收發、狀態轉移及完整決策條件。
5. **Failure**：至少一種 crash、delay、timeout、concurrent operation 或 network partition 情境（以適用於該技術為限）。
6. **Compare**：至少一張真正有區辨力的比較表，對比兩個相關機制的語義、成本、限制與典型用途。
7. **Validate**：手動核算範例，或提供可執行程式與預期結果（若確實需要），確認過程正確。
8. **Source**：講義頁碼 + 使用的論文／官方文件網址；延伸推導標為補充。

### 3.4 圖表與算例

- 時序、角色互動優先使用 Mermaid `sequenceDiagram`；狀態轉移用 `stateDiagram-v2`；架構拓樸用 `flowchart`。
- 每張圖附上文字解釋，避免只有圖沒有協定假設；圖若包含概念性省略，清楚註明。
- 範例應在圖、表、公式及文字間保持一致。可用三節點或五節點案例示範 Majority Quorum，明確寫出 `⌊N/2⌋ + 1`。
- 不要使用無來源的真實系統效能數字；如屬教學假設，標註「假設情境」。
- HackMD 與 GitHub 都應能顯示主要內容；避免將核心說明藏在僅本機可見的圖片連結中。

## 4. 已學習章節：必須涵蓋的主題與頁碼

### Chapter 00 — Course Introduction（P1–P17）

- 分散式系統的定義、主要動機及設計挑戰。
- 課程各單元的關聯、系統設計在一致性／可用性／容錯／效能上的取捨。
- 課程安排只根據實際投影片，不憑猜測更改考試規則。

### Chapter 01 — Logical Clocks, Global States, & Checkpointing（P18–P40）

- P21–P24：時間與因果順序、Lamport Clock 更新規則；完整多節點 timestamp 算例。
- P25–P27：Vector Clock 的更新／合併、向量比較、concurrent events，及 Lamport Clock vs. Vector Clock 表格。
- P28–P30：Global State、Consistent Cut 與 in-transit messages；以訊息傳送／接收的截面圖說明一致與不一致。
- P31–P34：Marker 的直覺、Chandy–Lamport Snapshot 完整步驟、channel state、前提（含 FIFO channel 的典型版本）。
- P35–P40：Checkpointing、Z-Cycle、Rollback-Dependency Graph、Rollback Recovery、Recovery Line；至少一個從初始 checkpoint 到選擇 recovery line 的逐步範例。
- 必須比較：Logical vs. Physical Clock、Lamport vs. Vector、Snapshot vs. Checkpoint、Consistent vs. Inconsistent Global State。

### Chapter 02 — Fault Tolerance, Paxos & Raft（P41–P62）

- P44–P46：Crash／Omission／Byzantine Fault 與 Asynchronous Network；failure detector 無法只憑 timeout 判定故障。
- P47–P49：Consensus 的 Safety／Liveness、FLP 的**正確假設與限制**；投影片示例是直覺，不應稱為 FLP 的形式證明。
- P50–P51：Proposer、Acceptor、Learner 的邏輯角色；一個實體伺服器可擔任多個角色。Learner 不計入 Acceptor Quorum。
- P52–P54：逐步推演 Prepare / Promise → Accept / Accepted → Chosen / Learned / Applied；附至少一張三角色訊息序列圖。
- P55–P57：三個角色的 lifecycle、逾時／重試、保存的狀態；區分 `promise number`、`accepted proposal number`、`accepted value`。
- P58：Happy Path，完整 `Prepare(10)`／`Promise(10, None)`／`Accept(10, A)` 範例。
- P59–P60：Competing Proposers、Adoption；示範收到 `(12, Y)` 且本輪為 `Prepare(20)` 時應發 `Accept(20, Y)`，並清楚解釋 **20 是本輪提案編號、12 是歷史提案編號、Y 才是沿用的值**。
- P61：Basic Paxos vs. Multi-Paxos、Replicated Log、Stable Leader 最佳化、Log Index 與 Proposal Number 的區別。
- P62：Raft 的 Leader Election、Log Replication、Safety；與 Basic Paxos、Multi-Paxos 做架構與訊息路徑比較。
- 必須明確區分 `Proposed`、單一 Acceptor 的 `Accepted`、多數 Acceptor 的 `Chosen`、Learner 的 `Learned`、應用的 `Applied`。
- **課程用語的精確性：** P54 將通知／學習結果稱為 Phase 3（Commit / Learn）；在經典 Basic Paxos 的標準核心共識描述中，Phase 1 與 Phase 2 為核心，學習／通知屬後續機制。此差異應以「課堂表示 vs. 演算法常見表述」註明，不可混為一談。
- **安全性提醒：** Quorum intersection 本身不等於完整 Safety 證明；還需 Promise 與歷史已接受值的選擇規則。Timeout 不代表提案必然未被 Chosen。
- 不要把「任意接受過的值」錯認為「已由多數選定的值」，也不要把「編號大的 Proposal」誤解成「數值上較大的 Value」。

## 5. 後續章節（P63 起）

- 從 P63 的 ZooKeeper 開始，**需重新讀取對應 PDF 範圍，按投影片及官方文獻逐段確認內容**，不能用一般教科書章節取代教授授課順序。
- 可以預先在 README 規劃 Chapter 03–09，但除非有明確任務，先不要自動產出尚未學習章節的完整內容。
- 後續主題可補充 ZNode／Watch／Session、P2P DHT／Gossip、Consistency Models／Transactions、LSM Tree／HBase、HDFS／MapReduce／YARN／Spark、Kafka，以及 Blockchain 的架構與故障模型；細節以實際 PDF 為準。

## 6. HackMD ↔ GitHub 協作規範

- **GitHub Repo 是 Codex 撰寫與版本控制的來源；HackMD 是閱讀、手動註解與分享介面。**
- HackMD 的 GitHub Sync 以**單篇 Note 對應單個 GitHub Markdown 檔案**為操作單位，不應假設 HackMD 資料夾會自動雙向同步整個 Repository。
- **對於已存在內容的 HackMD Note：** 先在 HackMD 備份並使用 **Versions and GitHub Sync → Push to GitHub**，建立對應的 `notes/*.md`，再由 Codex 從 GitHub 接續擴寫。
- **對於 Codex 先建立的新筆記：** 在 HackMD 新建空 Note，使用 **Versions and GitHub Sync → Pull from GitHub**，連結正確的 `repo / main / notes/filename.md`。
- 後續 Codex 修改並 Push → HackMD 手動 Pull；HackMD 若有編修，先在 HackMD Push，再讓 Codex `git pull --ff-only` 取得變更後繼續工作。
- **兩邊不要同時修改同一篇筆記卻未先同步。** 遇到差異先保存版本與人工確認，避免用覆寫解決衝突。
- HackMD 資料夾名稱、Note 標題、GitHub 路徑是不同概念；可重新整理 HackMD 資料夾，但不要因此推斷 GitHub 目錄會自動跟著更新。
- 建議對照：HackMD `checkpoint` → `notes/01-logical-clocks-checkpointing.md`；HackMD `Fault Telorant & Paxos & Raft` → `notes/02-fault-tolerance-paxos-raft.md`（GitHub 使用修正拼字的檔名）。
- 若 HackMD Note 已有使用者編輯內容，第一次連結時必須先備份／匯出，評估要 Push 還是 Pull，避免覆蓋原筆記。
- 使用 GitHub 相對連結組織 README；必要時在 HackMD 獨立維護入口索引，不要假設相對路徑跨平台有相同的導覽效果。

## 7. 完成與驗收標準（Definition of Done）

對每個完成的章節，至少檢查：

- [ ] 對應的講義頁碼與章節名稱正確。
- [ ] 核心定義、協定狀態、角色、數學符號、前提假設均清楚。
- [ ] 至少一個完整推演（含逐步狀態與訊息），而非僅描述概念。
- [ ] 常見故障／競爭／反例及恢復機制清楚。
- [ ] 存在必要的架構圖／時序圖與技術比較表。
- [ ] 關鍵 Safety／Liveness 結論與前提相容，不過度保證。
- [ ] 課程原文與延伸補充有來源層級區分，附可追溯出處。
- [ ] Markdown 標題層級、表格、程式碼塊及 Mermaid 語法可正常呈現。
- [ ] README 進度與連結已更新；未學習章節沒有被標記為完成。
- [ ] Git diff 經過檢查，未加入私有 PDF、金鑰、憑證或無關產物。

## 8. 首次執行建議（Codex 任務優先級）

1. 建立 `README.md` 章節索引及進度表；建立 `notes/`、`assets/` 結構；將 `reference/*.pdf` 加入 `.gitignore`。
2. 找到並核對重排後的 270 頁講義；若無法取得來源，停止宣稱「依據 PDF 完整整理」，明確列出缺件。
3. 優先寫作 Chapter 01（P18–P40），建立 Logical Clock、Vector Clock、Consistent Cut、Chandy–Lamport Snapshot、Rollback Recovery 的完整推演。
4. 接著寫 Chapter 02（P41–P62），詳述 Paxos 三角色完整互動、競爭提案、Adoption、Multi-Paxos／Raft 比較。
5. 補齊 Chapter 00（P1–P17）作為總覽，並更新 README 與交叉連結。
6. 逐章確認內容、圖表與來源；分批小 commit，最後列出完成檔案、頁碼與尚未完成的地方。

**核心品質原則：不是把 Slide 變成另一份 Slide；而是把 Slide 擴寫成能用來推導、除錯、設計與複習的完整工程筆記。**

## 9. 後續整理與編碼查核

- 各篇章首只保留標題，直接進入正文；課程身份、教材範圍、學習狀態、通用來源層級說明、上下章與 GitHub 備援導覽集中於 `notes/README.md`。各節具體頁碼與引用仍留在正文，不在章首重複專案資訊。
- 詳細頁序與來源指紋見 `reference/README.md`；更換 PDF 後重新核對。
- 英文單選題須附答案及每個選項的解析；重要演算法先完整推演，再提供速查。
- P60 原例是 `(10, X)`；`(12, Y)` 須另標為教學補充。Raft 的完整 RPC、日誌與安全性條件屬 P62 延伸，不冒充投影片原文。
- Markdown 一律以 UTF-8 儲存。Windows PowerShell 的文字管線可能將傳入 Python 的非 ASCII 字元替換成問號；避免使用未明確指定 UTF-8 的管線寫入中文。寫入後重新讀取並檢查內容。

## 10. HackMD 與 GitHub 雙平台相容性（必須遵守）

1. 所有提交至公開 Repository 的圖片統一放在 `assets/`，不散放於其他目錄。
2. Markdown 圖片使用 `https://raw.githubusercontent.com/johnson931128/Distributed-System/main/assets/檔名` 格式的完整 URL，不使用相對圖片路徑或本機路徑。檔名宜使用 ASCII，並保持大小寫一致。
3. 技術圖優先使用兩平台相容的 Mermaid 語法，避免平台專屬插件與初始化設定；SVG 顯示異常時匯出 PNG 備援，同樣放入 `assets/` 並使用完整 raw URL。
4. 檢查 Markdown 表格、公式、圖片、Mermaid 和跨章節連結在 GitHub／HackMD 的相容性。公式須定義符號，關鍵條件另提供文字或行內程式碼版本。GitHub 章節導覽可保留相對連結；HackMD 使用已知 Note URL，或完整 GitHub 文件連結作備援，不編造 Note URL。
5. 所有圖片必須先提交到 GitHub 後再驗證外部顯示；僅有本機 commit 或本機渲染不算外部驗證。尚未推送、raw URL 無法讀取或尚未在平台開啟時，須標示未驗證。本條本身不授權額外 push／發布操作。
6. HackMD 新建筆記時，若 GitHub 檔案已存在，應使用 **Versions and GitHub Sync → Pull from GitHub**，禁止以空白筆記 Push 覆蓋內容。已有人工編修者先備份、比較，再同步。
7. 所有圖片須附圖說，並記錄來源 URL、作者／組織、授權條件與必要署名；自製圖註明自製及技術依據。授權未確認者不提交，以原創圖替代。

驗證回報須分開列出「本機語法／渲染」「GitHub 實際顯示」「HackMD 實際顯示」，未執行者保留未驗證狀態。

## 11. Chapter 03／04 的來源與語義查核

- 使用者 2026-11-20 已明確授權向下整理兩章：P63–P89、P90–P117；P118 起仍需另行指示。筆記整理進度與使用者已學習進度分開。
- ZooKeeper 以 3.9.4 官方文件核對：Session 不等於單次 TCP；標準 Watch 是一次性失效通知；sync 並非無條件 quorum read；外部資源另需處理過期 lock holder。保留教材簡化並標明技術補充。
- Chord 的 key owner、finger start 與 routing hop 分開；Gossip 的單輪期望、大 N 近似、隨機執行與訊息成本分開。CFS 原始一般 Client 唯讀，P112 為可變資料共識的設計延伸，不說成 CFS 所有讀寫都跑 Paxos。
- 對原始 Chord maintenance 的一般收斂宣稱須考慮後續正確性研究與勘誤，不把單一加入圖當成任意 churn 的證明。新增論文留在 `reference/` 且不提交 PDF，公開索引記錄來源與雜湊。
