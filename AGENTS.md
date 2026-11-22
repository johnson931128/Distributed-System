# AGENTS.md — Distributed Systems 學習筆記專案規範

> Repository: `johnson931128/Distributed-System`  
> Language: 繁體中文（zh-TW），技術名詞保留英文；英文術語首次出現時附中文說明。  
> Main objective: 將國立成功大學 2026 Fall Distributed Systems 課程投影片，擴充成可供長期複習、理解原理、推演演算法與比較系統設計的技術筆記。  
> Target readers: 已具備作業系統、演算法、計算機網路及程式開發基礎的資訊／工程學生。  
> Current progress: 學習進度與筆記撰寫進度分開記錄，實際狀態以 `notes/README.md` 與使用者明確確認為準；不得把「已寫好」誤記為「已學會」。目前改版對象為現有 Chapter 00–04，不自動擴寫 P118 以後課程。

## 0. Agent 工作方式（必須遵守）

1. **先讀本檔，再檢查 Repository 既有檔案。** 修改既有筆記前先閱讀全文，避免覆寫人工編修與 HackMD 同步內容。
2. **先核對教材，再撰寫。** 不得只憑檔名、記憶或網路摘要，假裝已讀過教授的 PDF。沒有教材時應在輸出或進度回報明確標示缺少來源；不可杜撰投影片原文、頁碼或例題。
3. **課程教材決定章節與教學範圍；論文與官方文件負責補充實作、推導、架構及技術細節。** 補充內容不可冒充教授投影片原文。
4. **目前任務優先是既有筆記的教學式改版。** 先審閱 Chapter 00–04，挑一篇完成示範，再分章改寫；不因既有筆記「內容完整」而跳過可讀性重構，不擅自擴寫 P118 以後新課程。
5. **主要產物為易閱讀的 Markdown 教材。** GitHub／HackMD 相容；圖片依第 10 節的「成大講義／MIT 參考」來源規則選用。Mermaid 是工具，不是每張圖的預設答案；技術敘述不能退化成圖表與條列堆積。
6. **先使概念能被理解，再證明與深究。** 重要演算法應有可跟著走的正常案例、必要前提與關鍵故障情境；依教學需求逐步導入形式化細節，禁止每節機械式填滿同一套清單。
7. **改動前檢查 Git 狀態。** 不改動無關檔案、不強制推送、不任意刪除筆記。新增或重構多份筆記時先規劃章節和預期檔案；以小而可審查的 commit 提交。
8. **結束時回報**：修改檔案、對應 PDF 頁碼、補充來源、查核項目、尚待確認／尚未完成之處。未實際執行的命令或驗證不可宣稱成功。

## 1. 權威資料與引用規則

### 1.1 課程第一手來源（最高優先權）

- 課程：**Distributed Systems — Fall 2026**，National Cheng Kung University，Prof. Hung-Chang Hsiao（蕭宏章）。
- 主要教材：`reference/整包.pdf`，已核對為 270 頁合併講義；P18、P41、P63 分別為 Logical Clocks、Fault Tolerance、ZooKeeper 封面。
- 原文書：`reference/Distributed_Systems_4.pdf`，685 頁；van Steen 與 Tanenbaum，*Distributed Systems*，4th edition，題名頁 Version 4.03x（February 2025）。原文書實體頁碼須標為「原文書 PDF P…」。版本內部差異見 `reference/README.md`。
- 課程簡介以合併講義 P1–P17 為準；若另有拆分／重排的 PDF，先核對頁碼對應再引用，不預設名稱相同即代表頁序相同。
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
- MIT 6.5840（原 6.824）Distributed Systems 課程及 lecture notes／readings：https://pdos.csail.mit.edu/6.824/schedule.html（2026 春季頁面）；**作為參考資料，不能代替成大講義決定授課順序**。

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

## 3. 改版筆記的教學設計（優先於舊式百科整理）

### 3.1 內容目的與閱讀順序

**筆記不是逐頁翻譯、技術百科、論文註解集合，也不是考前速查表的放大版。** 成果應能從零連貫閱讀：讀者先理解「為何需要」，再看「系統如何運作」，最後能自行推演與辨認設計限制。

- **以講義確立主線**：先完整核對本章投影片，把連續幾頁回答的共同問題串成一節。講義給出的名詞、範圍、推進順序、例子與取捨必須保留；**一個概念群是一節，不是每張投影片一節**。
- **把各頁串成因果故事**：前一節提出的瓶頸，應自然引出下一節的解法。每個新機制先用一至兩段回答「前面的方法缺少什麼」「為何不直接沿用原方法」。
- **讀者體驗優先**：先交代場景和角色，再定義術語；專業名詞緊靠首次使用處以白話、操作及具體例子解釋。禁止連續丟出一串術語後才補字典。
- **正常案例先於故障反例**：先講完整的 happy path、狀態／訊息如何變化，再介紹 concurrency、crash、timeout、partition、形式化保證與失效邊界。
- **理論補充放在理解所需的地方**：教授一頁只說明方向時，可用原文書或原始論文補足推導，不應把所有嚴謹但次要的爭議和勘誤塞在第一段。
- **不要為縮短而省掉推理**：可刪冗言、重複提醒、冗長前言與過度表格化，但不可刪掉定義的判斷條件、重要狀態轉移、算例或必要安全前提。

### 3.2 每章先建立「投影片 → 概念鏈」

編輯前先做一份內部章節映射，至少記錄：(a) 講義頁碼與頁面主題，(b) 該頁回答的問題，(c) 本文對應小節，(d) 前後概念依賴，(e) 合適的教材圖片及原文書章節／論文。映射可放在工作紀錄；正文不需重現大型頁碼清單。

推薦每個主要概念群使用以下**彈性**節奏，不強制每節都放滿五種元素：

1. **問題與情境**：用短場景呈現原方法為何不足。
2. **核心原理**：嵌入精確的定義、必要條件、名詞如何運作，不做孤立名詞大全。
3. **可信的圖解**：說明角色、資料流、消息或時間軸；附一段真正引導閱讀圖的敘述。
4. **逐步演算或操作**：少量一致的節點、變數、訊息與數字，清楚指出每一步如何導向下一步。
5. **結果、取捨與銜接**：回答得到什麼保證、付出什麼成本，以及為什麼接下來要研究下一項技術。

章首用兩到四段解釋本章的核心問題與概念旅程；章尾再放少量比較、易混淆問題及自測題。不要在正文每段都加「考試重點」「值得注意」「但實際上」等固定標籤。

### 3.3 文字密度與版面約束

- 繁體中文為主；專有術語首次採 **中文（English）**，之後維持一致的名稱。新術語必須解釋**它負責什麼、如何操作、與上一個概念有何關係**。
- 以自然段落為主要敘述單位，每段聚焦一個可理解的問題。連續的大段堆疊、滿頁粗體術語、長串警告與一整節純表格，均視為待重寫。
- 標題反映問題或推理（例如「為什麼已有 IP Routing 還需要 Overlay？」）；避免全篇只是「定義／優點／缺點／比較／補充」的重複模板。
- 只有**比較多個選項**或**呈現固定欄位狀態**才用表格。時序演變優先圖或逐步案例，因果關係優先完整段落；不要以表格代替解釋。
- 程式碼／偽碼、公式與圖說需在正文解釋關鍵操作與變數。符號必須先定義，必要時手算至少一個非平凡案例。
- 必要 caveat 不能省，但應集中在相關概念理解之後的「適用前提／限制」段落，避免每一句結論後都接長篇例外情境。
- 正文避免稱呼讀者、AI 自述、浮誇語氣、空泛形容詞與無根據的效能斷言；文風應像一本清楚的教科書，**不是規格文件或稽核報告**。
- 習題放章末，優先 3–5 題能檢查因果與流程的英文 MCQ，附答案理由；試題不應超過本章核心說明的閱讀權重。

### 3.4 圖像策略：先有可信依據，再決定怎麼畫

**允許的視覺依據限定為：**

1. **成大教授提供的本章課程講義圖表**：頁碼與概念最直接匹配，優先選用。
2. **MIT 6.824／6.5840 的相關 lecture notes、slides 或其課程頁面連結的原始論文圖**：只作為補充比對；先確認它確實在說同一機制與假設。
3. **依上述教材自行重新繪製的教學圖**：簡化元素可以，但必須保持角色、箭頭、狀態與因果關係正確，並標明「自繪；參考成大講義 P…／MIT …」。禁止無來源即興畫出似是而非的協定圖。

**不以 AI 生成裝飾圖、隨機網路圖片、庫存素材或一般網路搜尋圖片充數。** 原講義與 MIT 的圖片**不代表可任意放入公開 GitHub**：直接截圖、下載、修改或重新發布前，須先確認具體圖片的可使用／再發布條件及必要署名；若無法確認，**不提交原圖**，改以原創忠實重繪或連結原始教材。重繪仍須避免照搬未獲許可的具創作性構圖。

選圖按機制選擇：架構用角色連線圖，訊息互動用時序圖，選舉／鎖用狀態變化，Snapshot 用時間軸，DHT 用 Ring／座標圖，Gossip 用輪次對照。圖的**數量取決於是否消除理解障礙**，不以每一頁必插圖充數。Mermaid 適合簡單流程／sequence；複雜拓樸或需要忠實呈現講義資訊時，優先使用可核對的 SVG／PNG 原創圖。每張圖都需有 caption、來源、圖中縮寫解釋及正文指引；沒有圖也應能讀懂核心機制。

### 3.5 原文書與補充資料的使用規則

- **主來源＝成大講義**，決定教學範圍、論述順序與課堂重點；**理論基礎＝van Steen／Tanenbaum《Distributed Systems》第 4 版**（本地檔 `reference/Distributed_Systems_4.pdf`）；**外部輔助＝MIT 6.5840 課程教材及對應原始論文／官方文件**。
- 補充原理時，優先從原文書定位精確章／節／PDF 頁碼，再用必要的原始論文解釋演算法條件；MIT 的教學組織與圖僅供改善講法，不可把 MIT 的內容冒充成大授課要求。
- 實際閱讀、核對過才能標示引用。至少在主要小節就近標註 `[課程講義] P…`，補充處標註 `[原文書] 第…章／§…／PDF P…`、`[MIT 教材] 標題 + URL` 或 `[原始論文]`。沒有取得完整來源或定位不到段落時，標「待查」，不得猜頁碼。
- 原文書擅長定義與理論解釋，論文擅長證明與實作條件；把其內容**消化成自己的連續論述與案例**，不貼整頁原文、不逐句翻譯大量外部文字。
- 講義的教學簡化與技術上更完整的條件若不完全相同，先忠實呈現講義，再以緊鄰而**簡短清楚**的「技術補充」說明差異；保留必要 Safety 前提，避免用大量枝節中斷主敘事。

### 3.6 品質示例：P2P／Overlay 章的理想銜接

應按教授的問題鏈串起 P93–P95：

**「Client-Server 將資源集中」→「P2P 動員邊緣 Peer」→「Peers 如何知道與誰交換資料？」→「建立 Overlay 的邏輯連線與應用層路由」→「邏輯連線底層仍走 IP，因此可能增加 latency」→「不修改 Router，也能讓 Peers 實作 ESM／ALM 多播」。**

談 Overlay 時必須回答兩個常見問題：**(1) 一次 Logical Hop 的耗時本來就包含底層 Physical Path 的傳輸與路由延遲；(2) Overlay 的主要目的不是美化拓樸圖，而是提供應用程式自主的資源發現、定位與轉送規則。** 將這些問答融入教科書式解說，避免孤立地在後面追加 Q&A 作補丁。

每個新章節建立類似的課程主線，並用**連接句**解釋從上一個技術到下一個技術的必要性。

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

## 5. 改版範圍與技術正確性

- **本輪只重構已存在的 Chapter 00–04**，保留章節檔名與連結穩定性；P118 之後的新單元要另獲明確要求才編寫。
- 參照第 4 節的逐章必備主題，不可因更追求可讀性而漏掉教授重要例題、關鍵規則或已驗證的錯誤修正。
- 推導和工業級邊界條件可移到章節後段「深入理解」或簡短補充，**不可將已核對的重要正確性警告刪掉**。
- 對既有筆記做內容盤點：每個知識點決定為「主線保留／後移／合併／刪除重複」，並保存關鍵技術差異與出處。
- 既有 Chapter 03／04 的 ZooKeeper Session／Watch／sync、Chord finger／owner、Gossip 模型與 CFS 角色差異，必須繼續遵守第 11 節查核條件。

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

每章重寫完成後，必須從**第一次接觸該主題的讀者**角度檢查：

- [ ] 第一頁能回答「本章為什麼存在」，並看得出教授投影片的完整概念路線。
- [ ] 相鄰主題有**因果過渡**；每個新增機制都交代前一個方法的限制，沒有只靠連續標題跳題。
- [ ] 重要名詞在首次出現時就有定義及操作說明；不必先查外部資料才能跟上例子。
- [ ] 至少有符合本章特性的**完整、可重算**的正常流程與一個必要反例；圖、文字、步驟的狀態一致。
- [ ] 圖解能解釋實際關係，圖中所有箭頭、角色、版本與時間概念正確；圖片來源及使用條件可追溯。
- [ ] 講義頁碼、原文書章節、MIT／論文的引用精確，並區分教授簡化與補充推導。
- [ ] 首輪閱讀不會遇到大片純表格、密集警告、連續技術名詞或段落堆疊；用章節導覽和短段落降低閱讀負擔。
- [ ] 形式化保證未被口語化改寫誤傷：Safety／Liveness、時間模型、Quorum、故障模型、複寫與 consistency 的必要前提仍成立。
- [ ] 在 GitHub／HackMD 可閱讀，Markdown、圖、公式、相對導覽、文字替代敘述均可檢查。
- [ ] 確認 diff、引用、檔名與 README 狀態；不得加入未獲確認可再發布的 PDF／原圖、金鑰或無關檔案。未執行的驗證不得宣稱完成。

**最後一項人工閱讀測試**：遮住章末速查與選擇題，僅讀正文，是否能自行說明「為什麼、如何操作、什麼時候失效、下一個機制解決什麼問題」？若不能，就算資料正確也不算改版完成。

## 8. Codex 改版執行順序（不得跳過）

1. **先審閱來源與現有筆記**：`AGENTS.md`、`notes/README.md`、`reference/README.md`、現有五篇 Chapter 00–04，並確認本地教材 PDF／MIT 連結可讀；不可只根據上一輪摘要動手。
2. **提出章節問題診斷與新結構**：列出每篇的主線斷點、名詞堆疊、圖解缺口、表格過量、重複 caveat，以及哪些技術細節應保留但後移。
3. **先重構 Chapter 04 作樣板**：因 P2P→Overlay→ESM→Napster→Gnutella→Gossip→DHT 具有清楚的教學因果鏈，最適合驗證新版文風、插圖策略與引用方式。
4. **再依序重構 Chapter 03、01、02、00**：每篇逐一完成、比對與檢查；尊重既有使用者修改，不要覆蓋剛新增的 Overlay 問答資訊。
5. **必要時同步 README 導覽**，但未學習的單元不得改為「已學習」，不要擴寫不存在的 Chapter 05–09。
6. **每章一組容易審查的 diff／commit**；若執行任務未明確授權 push，僅保留本地 commits 並回報。不得 force push 或自行更動 HackMD。
7. 結束提供「改版前後差異、保留的演算法與例題、圖片及其出處、教材覆蓋頁碼、驗證項目、尚需人工核對」。

## 9. 後續整理與編碼查核

- 各篇章首只保留標題，直接進入正文；課程身份、教材範圍、學習狀態、通用來源層級說明、上下章與 GitHub 備援導覽集中於 `notes/README.md`。各節具體頁碼與引用仍留在正文，不在章首重複專案資訊。
- 詳細頁序與來源指紋見 `reference/README.md`；更換 PDF 後重新核對。
- 英文單選題須附答案及每個選項的解析；重要演算法先完整推演，再提供速查。
- P60 原例是 `(10, X)`；`(12, Y)` 須另標為教學補充。Raft 的完整 RPC、日誌與安全性條件屬 P62 延伸，不冒充投影片原文。
- Markdown 一律以 UTF-8 儲存。Windows PowerShell 的文字管線可能將傳入 Python 的非 ASCII 字元替換成問號；避免使用未明確指定 UTF-8 的管線寫入中文。寫入後重新讀取並檢查內容。

## 10. 圖片發布與 GitHub／HackMD 相容性

1. 公開 Repo 中允許發布的圖片統一放在 `assets/`，以可辨識名稱及章節分組（例如 `assets/diagrams/ch04-overlay-ip-path.png`）。不得附帶講義／原文書 PDF。
2. **圖解內容的參考來源只限第 3.4 節所述的成大講義與 MIT 6.824／6.5840 相關材料**；若直接重用圖片，先確認該張圖片的權利條件、必要署名與可重製範圍；未確認時選擇有出處的原創重繪或只附原始來源連結，不可假定課程公開即可自由轉貼。
3. 圖片的正文上下必須解釋如何閱讀，附來源頁碼／課程 URL、圖說、使用／重繪註記及可讀的 alt text。圖片不能成為唯一講授途徑。
4. 外部圖片 URL 使用完整 `https://raw.githubusercontent.com/johnson931128/Distributed-System/main/assets/...`；在檔案尚未 push／URL 尚不可存取前，記錄為**未驗證**，不要聲稱已能在 HackMD 顯示。若因未 push 不便預覽，先用本機相對路徑編輯，發布時再改成正式路徑。
5. Mermaid 可用於簡單流程與時序，但必須檢查 GitHub／HackMD 相容性；需要精確配色、路線、環狀拓樸或多欄狀態圖時可採原創 SVG／PNG，必要時提供 PNG 備援。
6. HackMD 每篇筆記與一個 GitHub Markdown 檔案對應；Codex 改寫後的 GitHub 版本先經人工比對，再由 HackMD Pull。已有 HackMD 編輯時先備份／同步，不能以空白 Note Push 覆蓋。
7. 驗證報告須分開「本機 Markdown／圖片檢查」「GitHub 實際渲染」「HackMD 實際渲染」三類，不可拿 Markdown 解析成功代替已測過線上畫面。

## 11. Chapter 03／04 的來源與語義查核

- Chapter 03／04 已有完整技術筆記，**本輪授權的是把現有筆記改成可閱讀的教學教材**，不是增寫 P118 起的課程。筆記整理進度與實際學習進度分開。
- ZooKeeper 以 3.9.4 官方文件核對：Session 不等於單次 TCP；標準 Watch 是一次性失效通知；sync 並非無條件 quorum read；外部資源另需處理過期 lock holder。保留教材簡化並標明技術補充。
- Chord 的 key owner、finger start 與 routing hop 分開；Gossip 的單輪期望、大 N 近似、隨機執行與訊息成本分開。CFS 原始一般 Client 唯讀，P112 為可變資料共識的設計延伸，不說成 CFS 所有讀寫都跑 Paxos。
- 對原始 Chord maintenance 的一般收斂宣稱須考慮後續正確性研究與勘誤，不把單一加入圖當成任意 churn 的證明。新增論文留在 `reference/` 且不提交 PDF，公開索引記錄來源與雜湊。
