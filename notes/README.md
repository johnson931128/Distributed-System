# 學習筆記目錄

## 課程、教材與閱讀範圍

[課程講義] National Cheng Kung University，Prof. Hung-Chang Hsiao，Distributed Systems，Fall 2026。本機教材 `reference/整包.pdf` 共 270 頁；所有課程 P1–P270 均指此檔 **1-based 實體頁碼**，不採各 deck 頁尾的局部編號。

使用者已確認的閱讀進度為 **P1–P62 已學習，P63 為待閱讀起點**。Chapter 00–04 均已完成教學改版，03／04 待閱讀。每章末尾的對照表列出投影片、教學主題、圖解、算例和銜接問題。下一個整理單元為 P118 的 Consistency。

原文書為 van Steen、Tanenbaum 的 *Distributed Systems*，4th edition，題名頁 Version 4.03x，共 685 頁。教材差異、來源指紋與頁碼對應見 [教材核對紀錄](../reference/README.md)。原始 PDF 留在本機，不公開提交。

## 章節導覽

| 章節 | 講義範圍 | 筆記與內容 | 學習／撰寫狀態 | HackMD |
| --- | --- | --- | --- | --- |
| 00 | P1–P17 | [Course Introduction](00-course-introduction.md)：課程定位、設計取捨、課程安排、練習題 | 已學習／已撰寫 | 待連結 |
| 01 | P18–P40 | [Logical Clocks, Global States & Checkpointing](01-logical-clocks-checkpointing.md)：時鐘核算、Marker、Z-Cycle、Recovery Line | 已學習／已撰寫 | 待連結 |
| 02 | P41–P62 | [Fault Tolerance, Paxos & Raft](02-fault-tolerance-paxos-raft.md)：協定狀態、完整訊息路徑、競爭、Adoption、Raft 日誌安全性 | 已學習／已撰寫 | 待連結 |
| 03 | P63–P89 | [ZooKeeper](03-zookeeper.md)：ZAB、Session、Watch、Lock 與 fencing | 待閱讀／已整理 | 待連結 |
| 04 | P90–P117 | [P2P & Gossip](04-peer-to-peer-gossip.md)：Push／Pull、CAN、Chord、CFS 與安全邊界 | 待閱讀／已整理 | 待連結 |
| 05 | P118–P155 | Consistency, Replication & Transactions | 待學習／未展開 | 待連結 |
| 06 | P156–P182 | LevelDB & HBase | 待學習／未展開 | 待連結 |
| 07 | P183–P210 | HDFS, MapReduce, YARN & Spark | 待學習／未展開 | 待連結 |
| 08 | P211–P238 | Kafka & Stream Processing | 待學習／未展開 | 待連結 |
| 09 | P239–P270 | Blockchain Foundations | 待學習／未展開 | 待連結 |

閱讀順序為 00 → 01 → 02 → 03 → 04；沒有建立 P118 起的空白章節檔案。03 的上一章為 02、下一章為 04；04 的下一單元 Consistency 仍待展開。

## 來源層級與算例標示

- `[課程講義]`：決定本章範圍、原例與考點；各節保留具體頁碼。
- `[原始論文／官方文件]`：補足精確假設、狀態、規則及實務語義；文件版本或查閱日期列於各章。
- `[教學補充／推導]`／「延伸補充」：自製例子、正確性解釋與超出投影片的細節，不冒充教授原文。
- `[待確認]`：無法由已讀來源確定的資訊，不能寫成已查核事實。

除標為「講義原例」者外，筆記的圖、數值案例、時間軸與選擇題皆為自製。Mermaid 為原創重繪，技術依據見所在小節，未複製課程整頁或使用授權不明的外部圖片。

## 各章需要保留的來源差異

1. Chapter 00：課程安排依 P1–P17；P15 明列暫定性，未宣稱已核對最新公告。
2. Chapter 01：P18 封面寫 Week 2，P16 課表排在 Week 1，引用一律依實體頁碼。P24／P26 為同一組訊息箭頭的兩種時鐘；P33 為轉帳 50 的原例。其他 Domino 推演另標補充。
3. Chapter 02：P54 的 Phase 3 是課堂 Commit／Learn 表述，經典核心為 Phase 1／Phase 2。P60 原例為 `(10,X)`，`(12,Y)` 為自製案例。Raft 的 Term、RequestVote、AppendEntries、Commit Index 與完整 Safety 條件是 P62 的論文延伸。
4. Chapter 03：P78 的四個 voting servers 需要三票；兩個 follower ACK 需加上 Leader 自身。P87 的 TCP 失聯與 ZooKeeper Session 到期需區分。P88 的 sync 強保證與 3.9.4 官方文件有差異，正文保留課堂表述再補充限制。P89 預告 Week 8，但 PDF 下一份實際為 P90 的 P2P。
5. Chapter 04：P99–P103 的公式採理想 round 模型，期望、近似與訊息成本分開。P107 的 key42 owner 是 N45；finger start 不是現存節點 ID。P112 的可變資料 Paxos 群體另列為延伸，不冒充原始唯讀 CFS。Chord 原始 maintenance 的一般正確性宣稱另以 Zave 後續研究限定。

## GitHub 與 HackMD 導覽備援

GitHub 內使用上方相對連結。HackMD 的章節 Note URL 未知，先保留「待連結」；若相對路徑不能導覽，可使用：

- [GitHub 專案入口](https://github.com/johnson931128/Distributed-System)
- [Chapter 00 完整 URL](https://github.com/johnson931128/Distributed-System/blob/main/notes/00-course-introduction.md)
- [Chapter 01 完整 URL](https://github.com/johnson931128/Distributed-System/blob/main/notes/01-logical-clocks-checkpointing.md)
- [Chapter 02 完整 URL](https://github.com/johnson931128/Distributed-System/blob/main/notes/02-fault-tolerance-paxos-raft.md)
- [Chapter 03 完整 URL](https://github.com/johnson931128/Distributed-System/blob/main/notes/03-zookeeper.md)
- [Chapter 04 完整 URL](https://github.com/johnson931128/Distributed-System/blob/main/notes/04-peer-to-peer-gossip.md)

這些是預定的 Repository 文件路徑；本機 commit 尚未 push 前，不能假定線上已存在。每篇新 HackMD Note 應從既有 GitHub 檔案 **Pull**；不可用空白 Note Push 覆蓋 GitHub。

後續待辦：使用者閱讀新增兩章；另獲明確任務後整理 P118 起教材；建立實際 HackMD 連結；發布後分別驗證兩平台的表格、公式、圖與跨章節導覽。完整同步與圖片 URL 規則見根目錄 `AGENTS.md`。
