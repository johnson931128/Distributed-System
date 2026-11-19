# Chapter 00 — 課程簡介與系統設計視角（Course Introduction）

## 1. 分散式系統要解決什麼問題？

> 課程依據：P3–P5。

**分散式系統（Distributed System）** 由不同電腦上的元件組成，透過網路訊息溝通與協調。它並非「很多程式同時跑」就自然成立；讀者需要知道資料與責任在哪些節點、跨節點訊息如何影響狀態，以及失聯時誰仍能作決定。

將服務拆到多台電腦，可以共享資源、分散儲存與計算負載，也可利用副本減少單點故障的影響。但拆分同時引入訊息延遲、重試、部分故障與相互矛盾的觀測。效能與容錯是設計目標，不是增加機器數就自動獲得的保證。

P3 從 Client–Server、P2P、Cloud Computing 到 Decentralized Ledgers 說明系統演進，並列出 MapReduce、HBase／Cassandra、Kafka、Blockchain 等應用。這些系統共用許多原理，卻不採用完全相同的故障模型、資料介面或一致性保證。

P4–P5 的課程定位是先建立理論，再觀察實務系統如何實現機制；不以逐行拆解所有專案原始碼為目標。分析一個系統時，應先問問題與保證，再對照架構，最後才談個別 API。

## 2. 用一個訂單服務看取捨

> [教學補充／推導] 依 P3–P6 的原理與系統對照，自製假設情境；不是講義原例或實測產品。

假設 Client 送出訂單，A 為處理節點，B 為副本，庫存只剩 1 件。一次正常路徑可以是：

1. Client 產生唯一 `request_id=r1`，送到 A。
2. A 檢查請求、協調命令順序，將「嘗試扣一件庫存」寫入複寫流程。
3. 達到該協定規定的提交條件後，狀態機按順序執行；庫存 1→0。
4. A 保存 r1 的結果，再回覆成功。B 按協定追上相同命令與狀態。

```mermaid
sequenceDiagram
    participant C as Client
    participant A as 處理節點 A
    participant G as 複寫與協調群體
    C->>A: 訂單 r1
    A->>G: 決定命令順序並複寫
    G-->>A: 達到指定提交條件
    Note over A: 依序執行，保存 r1 結果
    A-->>C: 成功
```

圖中的 G 不是單一副本 ACK 就必定足夠；具體 quorum 與狀態規則由 Chapter 02 說明。此圖只建立「請求、提交、執行、回覆」的依賴。

### 2.1 回覆遺失與部分故障

若步驟 4 的回覆遺失，Client 只看到 timeout，卻不知庫存是否已扣。直接用新 ID 下第二張單，可能造成重複訂單；以相同 r1 重試，並讓狀態機保存去重結果，才能判斷是否已處理。

若 A 與 B 失聯，但各自接受「最後一件庫存」的訂單，兩邊可能都宣稱成功。改為失聯時暫停部分寫入，能保護某些一致性要求，代價是這部分請求暫時無法完成。是否允許超賣、是否採補償，是應用語義，不能由「有兩份資料」推得。

若 A 扣款後、B 入帳前各拍一張備份，可能少算在途款項；恢復時又可能收到沒有對應傳送紀錄的訊息。Chapter 01 的 Consistent Cut 與 Snapshot 正是處理這種全域狀態問題。

### 2.2 架構比較

| 設計 | 可取得的好處 | 明確成本與限制 | 需再回答的問題 |
| --- | --- | --- | --- |
| 單節點保存全部狀態 | 本地排序與交易邊界較單純 | 節點故障會中斷服務；受單機資源限制 | 如何持久化與備份？ |
| 非同步複寫 | 回覆可不等待遠端持久化；讀副本可分散流量 | failover 可能缺少尚未複寫的更新；讀值可能落後 | 接受多少資料遺失與讀取延遲？ |
| 協調式日誌複寫 | 在故障模型與 quorum 規則內保護已提交順序 | 寫入需跨節點往返與可靠保存；失去多數時停止進展 | 如何選 Leader、恢復歷史與提供讀取？ |
| 分區儲存（Sharding） | 不同鍵由不同節點承擔，分散容量與負載 | 跨分區操作需額外協調；hot key 仍可能集中 | 鍵如何路由與遷移？跨分區交易如何完成？ |

分區儲存與網路分區（Network Partition）是兩個不同概念：前者是主動分配資料，後者是網路故障造成的隔離。它們可以同時出現。

## 3. 課程各單元的原理連結

> 課程依據：P6、P16–P17。以下以主題整理，不以 P6 的週次取代正式課表。

| 核心原理 | 為何會反覆出現 | 課程中的系統連結 |
| --- | --- | --- |
| 共識與多數決（Consensus & Quorum） | 跨故障與競爭維持共同決定 | Paxos、ZooKeeper、儲存管理與 Blockchain |
| 一致性模型（Consistency Models） | 明定 Client 能觀察到何種順序與值 | 分散式資料庫、DHT、複寫系統 |
| 附加式日誌（Append-Only Log）與全序廣播（Total Order Broadcast） | 讓事件可依序傳播、重播與恢復 | ZAB、交易日誌、Kafka 等；具體語義不全相同 |
| 快照與回復（Snapshot & Recovery） | 故障後保留合法狀態、控制重做工作 | Chandy–Lamport、儲存與運算系統 |
| 邏輯時間（Logical Time）與多版本控制（Multi-Version Concurrency Control，MVCC） | 區分事件與資料版本關係 | Vector Clocks、版本化資料管理 |
| P2P 路由與 Gossip | 在大量參與者間尋址與傳播資訊 | DHT、Gossip、Blockchain 網路 |

P6 是原理對應表，不表示同一列的系統都實作相同協定。例如 Kafka ISR 不應直接視為 Basic Paxos 的 Acceptor Quorum，ZAB 也不等於 Basic Paxos。後續章節要重新讀各自講義與官方文件。

## 4. 課程安排與評分：忠實保留暫定性

> [課程講義] P1–P2、P7–P17。本節只記錄 PDF 上的課程政策；不是即時課務公告。

課程為 National Cheng Kung University，Prof. Hung-Chang Hsiao（蕭宏章），Fall 2026。P2 寫週五 09:00–12:00、以連續 150 分鐘授課區段進行，並允許彈性個人移動；助教 TBA，沒有指定必備教科書。時段與實際授課區段照原頁記錄，不自行補出休息規則。

### 4.1 評分與試題形式

| 項目 | P7 的比例與規則 |
| --- | --- |
| Written Examination | 70%；Week 13，20 題單選 |
| Student Presentation | 20%；小組專題或文獻報告 |
| Attendance | 10%；每次點名 1%，最多 10% |

P10 補充考試為全英文單選。P8–P10 的示例分別測 Marker 邊界、ZooKeeper 避免 Thundering Herd 的前驅觀察策略、Paxos 歷史值採用；本次只在對應已學章節展開推理，ZooKeeper 原理留後續。

**P15 明確說明以上政策、評分與週次均為暫定，可能依實際教學調整。** 本地 PDF 不證明目前實際課務仍未修改。

### 4.2 小組報告與主題

P11：全班 12 組，每組約 5 人；每組 25 分鐘，含 18 分鐘報告、5 分鐘 Q&A、2 分鐘換場。上台主講限一人，其餘組員可參與 Q&A。題目先選先得。評分看機制能否對應理論、架構與時間控制；微型叢集類另看展示流暢度與容錯驗證。

| 分類 | P12–P13 的四個方向 |
| --- | --- |
| Paper Review | Google Spanner、Raft、Amazon Dynamo、PBFT |
| Architecture Analysis | Apache Pulsar vs. Kafka、Redis Cluster、Elasticsearch、TiDB |
| Mini-Project & Live Demo | ZooKeeper 容錯與選舉、Spark RDD 容錯、HDFS NameNode 高可用性、分散式鎖與狀態還原 |

P12 對 Raft 報告方向寫「原論文中未提及」的 Membership Change 與日誌壓縮；**技術補充／更精確說法**：已核對的 [Raft Extended Version](https://raft.github.io/raft.pdf) 實際在 §6、§7 討論這兩者。因此把它理解為報告深化主題，不能引用成「Raft 原論文完全沒有這些內容」。

P14 建議 3–4 節點，示意為 1 Master 加 2–3 Workers；每節點至少 2 vCPU、4 GB RAM、20 GB Disk。這是教材建議，不是各產品的正式最低需求或保證。該頁另提 GCP 新戶額度與 GitHub Student Developer Pack；雲端優惠會變動，本筆記不將其當成已查證的當前方案，也不以此安排付費資源。

### 4.3 逐週課表

以下依 P16–P17，日期照投影片列示；不表示本筆記已完成該週內容。

| Week | 日期 | 主題／安排 |
| --- | --- | --- |
| 1 | 09/11 | Introduction、System Models、Logical Clocks & Global States |
| 2 | 09/18 | Instructor Away／External Speech；No Class |
| 3 | 09/25 | Mid-Autumn Festival；No Class |
| 4 | 10/02 | Fault Tolerance & Paxos |
| 5 | 10/09 | National Day Substituted Holiday；No Class |
| 6 | 10/16 | ZooKeeper |
| 7 | 10/23 | P2P & Gossip |
| 8 | 10/30 | Consistency、Replication、Transactions |
| 9 | 11/06 | Departmental Review／Flexible Learning；No Class |
| 10 | 11/13 | LevelDB & HBase |
| 11 | 11/20 | HDFS、MapReduce、YARN、Spark |
| 12 | 11/27 | Kafka／Stream Processing |
| 13 | 12/04 | Blockchain 與 Written Examination |
| 14 | 12/11 | Student Presentations I |
| 15 | 12/18 | Student Presentations II 與 Course Conclusion |
| 16 | 12/25 | Constitution Day；No Class |
| 17 | 01/01 | Founding Day；No Class |
| 18 | 01/08 | Flexible Learning；No Class |

P18 deck 封面寫 Week 2，與上述安排不同；P6 的部分系統週次也不同。引用筆記時以實體頁碼與標題為定位，不推測是否由不同版本的課表合併而來。

## 5. 如何閱讀後續技術筆記？

> [教學補充／推導] 對照 P4–P6 的「原理 → 架構 → 應用」目標。

閱讀任何協定時先固定模型：節點是否只會 crash？網路是否 FIFO？哪些資料已可靠落盤？接著列出角色、狀態與訊息；逐步記錄何時某個結果只是被一台接收、何時已滿足協定決定條件、何時應用真正執行。

驗證不只看正常路徑。應把 crash 放在「保存前／保存後」「送出前／送出後」「多數完成但通知前」等位置，檢查重試是否仍滿足不變量。比較方案時，則指出需要多少控制訊息、同步儲存與回復工作，而不是只寫快慢。

本次閱讀順序：先以 Logical Clocks 理解因果，再用 Snapshot 理解一致全域狀態，最後以 Paxos／Raft 理解如何在故障與競爭中決定共同命令。P63 的 ZooKeeper 是下一單元起點，尚不展開。

## 6. 常見誤解與重點速查

| 誤解 | 修正 |
| --- | --- |
| 有多台副本就有容錯 | 還需定義故障模型、提交條件與恢復方式 |
| 網路沒回覆表示請求沒執行 | 可能已提交但回覆遺失 |
| 所有系統的 Log 都代表同一種保證 | 記錄結構相似，不代表提交、複寫與回復語義相同 |
| 本機最新備份可以直接拼成全域最新備份 | 跨節點可能出現 orphan 與遺失在途訊息 |
| 投影片課表就是永久固定政策 | P15 保留動態調整 |

速查：描述系統要同時交代「資料在哪裡、訊息如何走、何時算完成、故障時如何恢復」。課程以理論支撐架構分析；本地原文書是補充來源，不是 P2 所稱的指定必備教科書。

## 7. 英文選擇題與逐項解析

以下為自製練習，不是教授原題。

### Q1 — Partial failure

Which scenario best illustrates partial failure in a distributed system?

- A. One server is unreachable while other servers continue processing requests.
- B. Every component is guaranteed to stop at exactly the same time.
- C. A local variable is renamed without changing behavior.
- D. Two processes on one host always share the same state.

**答案：A。** A：系統仍局部運作，符合定義。B：全體同時停止不呈現部分可達的困難。C：不是故障行為。D：不是分散式故障模型，也非一般程序保證。

### Q2 — Replication

Why is copying data to multiple servers insufficient by itself to guarantee a consistent service?

- A. Replicas cannot communicate over networks.
- B. Replicas may observe concurrent requests in different orders unless a protocol defines the required behavior.
- C. Every replicated service must use Blockchain.
- D. Physical clocks automatically determine a unique correct command order.

**答案：B。** A：複寫本來可透過訊息。B：命令順序與故障行為需要協定。C：有多種複寫與協調方法。D：時鐘誤差與並行操作不能自動解決應用競爭。

### Q3 — Course policies

How should the grading percentages and weekly schedule in the introduction slides be interpreted?

- A. They are permanent guarantees unaffected by later announcements.
- B. They may be freely replaced with a generic university policy.
- C. They are the policies recorded in the provided slides and are explicitly tentative.
- D. Their presence proves that every listed chapter has already been studied.

**答案：C。** A：違反 P15 的暫定聲明。B：不能以無來源政策替換教材。C：保留來源與效力界線。D：課表規劃不等於閱讀進度。

### Q4 — Timeout and retry

A client times out after submitting an order. Which design most directly helps prevent duplicate execution when it retries?

- A. Treat every retry as a new unrelated order.
- B. Assume a timeout proves that no state changed.
- C. Remove all durable records to make the retry faster.
- D. Reuse a unique request ID and preserve the processed result in the service's state.

**答案：D。** A：可能重複處理。B：無法從無回覆推得未執行。C：破壞恢復與去重資訊。D：讓服務辨認同一邏輯請求；仍需可靠保存與正確複寫。

## 8. 參考資料與投影片對應

| 頁碼／來源層級 | 內容 |
| --- | --- |
| [課程講義] P1–P5 | 課程身份、基本資訊、系統定義與教學方法 |
| [課程講義] P6 | 原理與系統的對照 |
| [課程講義] P7–P10 | 評分、英文單選示例與考試形式 |
| [課程講義] P11–P14 | 報告規則、主題、微型叢集資源建議 |
| [課程講義] P15–P17 | 暫定政策聲明與逐週課表 |
| [原始論文／延伸補充] | [Raft Extended Version](https://raft.github.io/raft.pdf)，§6–§7，核對 Membership Change 與 Log Compaction 確有討論 |

教材身份、頁序與版本差異集中在 [教材紀錄](../reference/README.md)；本章課程政策只依提供的 PDF，未宣稱核對過最新課務公告。
