# 本機教材與頁序核對紀錄

核對日期：2026-11-19。使用 PyMuPDF 核對頁數、書籤與逐頁文字；另渲染並檢視 P24、P26、P30、P33、P36–P38、P40、P59–P60 的圖表。筆記中的課程 `P…` 一律指合併講義的 **1-based 實體頁碼**。

## 兩份 PDF 的身份

| 本機檔案 | 實體頁數 | 實際內容 | 用途 |
| --- | --- | --- | --- |
| `reference/整包.pdf` | 270 | NCKU，Hung-Chang Hsiao，Distributed Systems，Fall 2026；10 個依章節排列的 slide decks | 決定課程順序、範圍與引用頁碼 |
| `reference/Distributed_Systems_4.pdf` | 685 | Maarten van Steen、Andrew S. Tanenbaum，Distributed Systems，Fourth edition；題名頁為 Version 4.03x（February 2025） | 補充原理與工程背景 |

原文書依 Introduction、Architectures、Processes、Communication、Coordination、Naming、Consistency and replication、Fault tolerance、Security 排列，後接 Index、Bibliography、Glossary。它與講義有 Logical Clock、Vector Clock、Raft、Paxos、Recovery 等主題重疊，但不是同一份教材的不同頁序版本。不可互換頁碼。

比對兩份 PDF 的非空整頁文字，移除空白並轉小寫後，完全相同的頁面為 0。此結果只代表整頁文字比對，不是圖像或逐句重複鑑定。

### 原文書的版本與頁碼差異

- PDF P1 封面為 4th edition / Version 03；P3 題名頁為 4.03x / February 2025。
- PDF P5 版權頁仍寫 Edition 4 / Version 02 / February 2024；本文頁腳為 DS 4.03x。保留這項內部差異，不推測所有內頁都已統一更新。
- PDF P17 起印刷頁碼為 1。本次使用範圍的實體頁碼為印刷頁碼加 16；引用時明寫「原文書 PDF P…（印刷 p.…）」。
- [作者官方書籍頁](https://www.distributed-systems.net/index.php/books/ds4/)提供第四版介紹與個人化電子書取得方式；免費取得不代表可以再散布。

| 對應筆記 | 原文書章節 | 實體頁碼／印刷頁碼 | 本次使用方式 |
| --- | --- | --- | --- |
| Chapter 00 | Ch.1 Introduction | PDF P17–P70 / pp.1–54 | 目錄定位；課程安排只依講義 |
| Chapter 01 | §5.2 Logical clocks | PDF P276–P287 / pp.260–271 | Lamport、Vector 與因果歷史 |
| Chapter 01 | §8.6 Recovery | PDF P552–P558 / pp.536–542 | Checkpoint、Domino、Message Logging |
| Chapter 02 | §5.4.4 Raft election | PDF P305–P306 / pp.289–290 | 選舉直覺；完整條件另依原論文 |
| Chapter 02 | §8.2.3–§8.2.4 | PDF P491–P506 / pp.475–490 | Raft、Paxos 與簡化描述的界限 |

原文書 PDF P500 的簡化說明允許 Acceptor 通知後忘記值；本筆記採課程與 Paxos 原論文的持久記憶要求，不能直接據此刪除 Accepted 狀態。原文書 PDF P493–P494 明示簡化 Raft；本筆記另外區分 Replicated、Committed、Applied，並依原論文補足選舉與提交條件。

## 講義章節邊界

| 實體頁碼 | 章節封面 |
| --- | --- |
| P1–P17 | Course Introduction |
| P18–P40 | Logical Clocks, Global States, & Checkpointing |
| P41–P62 | Fault Tolerance & Paxos Consensus Algorithm |
| P63–P89 | Distributed Coordination Services (ZooKeeper) |
| P90–P117 | Peer-to-Peer Computing (Overlay Networks) |
| P118–P155 | Data Consistency, Replication & Distributed Transactions |
| P156–P182 | LevelDB and HBase: Distributed Storage Engines |
| P183–P210 | Distributed Storage and Resource Management |
| P211–P238 | Distributed Data Streaming Architectures |
| P239–P270 | What is Blockchain and Its Foundations |

上述封面與 PDF 書籤起點一致，各章結尾也已抽取確認。P63 起僅核對結構，未據此宣稱完成後續章節閱讀。

## P1–P62 內容對照

| 頁碼 | 已讀取的主題 |
| --- | --- |
| P1–P5 | 課程身份、資訊、分散式系統定義、設計理念 |
| P6–P10 | 理論與系統對應、評分、三類英文單選題示例 |
| P11–P15 | 報告規則、12 個主題、運算資源建議、暫定政策 |
| P16–P17 | 全學期課表 |
| P18–P20 | Logical Clocks 章封面、定位、Roadmap |
| P21–P24 | 因果動機、Logical Clock、Lamport 更新與圖例 |
| P25–P27 | Vector Clock、圖例與比較規則 |
| P28–P30 | Global State、Consistent Cut、C1／C2 圖例 |
| P31–P34 | Marker、Chandy–Lamport、轉帳算例、性質 |
| P35–P37 | Checkpoint、三節點時間軸、Z-Cycle |
| P38–P40 | Rollback-Dependency Graph、選擇快照、Recovery Line |
| P41–P43 | Fault Tolerance 章封面、定位、Roadmap |
| P44–P46 | Partial Failure、Fault Models、Asynchronous Network |
| P47–P49 | Consensus、FLP 與直覺示例 |
| P50–P51 | Paxos 三角色與實體部署 |
| P52–P54 | Prepare／Promise、Accept／Accepted、Commit／Learn |
| P55–P57 | Proposer、Acceptor、Learner lifecycle |
| P58–P60 | Happy Path、Competing Proposers、Adoption |
| P61–P62 | Multi-Paxos 與 Raft 概覽 |

## 必須保留的差異與限制

1. P18 deck 封面寫 Week 2，P16 課表卻將 Logical Clocks 排在 Week 1；P6 的部分系統週次也與 P16–P17 不同。筆記依實體頁序組織，不擅改教授週次。
2. P31 的「Domino effect」形容 Marker 連鎖傳遞，與 P40 的 cascading rollback／Domino Effect 不是同一種故障現象。
3. P49 是 FLP 直覺，不是形式證明；不能推成「少一票就絕對不能決定」。
4. P54 用 Phase 3 表示 Commit／Learn；經典 Basic Paxos 核心為 Phase 1 與 Phase 2。P53 的 Commit 標題不代表單一 Acceptor Accepted 就是 Chosen。
5. P59 與 P60 應作競爭與恢復情境閱讀。安全補全 P60 時，回報 `(10, X)` 的 Acceptor 必須在新 Proposer 採用的 Phase 1 quorum 中；同一提案編號不得先發出一值後又改發另一值。
6. P60 原例是 `(10, X)`，不是 `(12, Y)`；後者在筆記另標為自製範例。
7. 合併 PDF 的 P145、P205、P207、P208 抽取時回報遺失 XObject resource，均在本次範圍外。未修改原始檔；後續整理前須確認圖形是否缺失。P1–P63 未出現此類解析警告。
8. 未提供獨立 Intro_Slides.pdf；本次課程簡介直接依合併 P1–P17。

## 來源指紋

更換或重排檔案後須重新核對。

```text
整包.pdf
SHA-256 1f314ab59786803ef5c492cfe4a73e022ffd7f16d2c61c68b868847b10431ee2
Distributed_Systems_4.pdf
SHA-256 cc3e33241bd6c9d54eb987fedc655206e5548667d68184d6b5cb76a2d127b408
```

兩份 PDF 留在本機，不提交公開 Repository。

## 已下載的引用論文

下載日期：2026-11-19。以下 8 篇涵蓋目前 `notes/` 實際引用的所有論文 PDF URL；下載自作者、研究機構或原研究團隊的公開來源。原始檔直接存於本目錄，均受 `reference/*.pdf` 忽略規則保護。公開索引保留來源連結，不依賴本機 PDF 連結。

| 本機檔名 | 論文與下載來源 | PDF 實體頁數 | 對應筆記 |
| --- | --- | --- | --- |
| `lamport-1978-time-clocks.pdf` | Lamport，1978，[Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) | 8 | Chapter 01：事件偏序、Logical Clock |
| `chandy-lamport-1985-distributed-snapshots.pdf` | Chandy、Lamport，1985，[Distributed Snapshots: Determining Global States of Distributed Systems](https://lamport.azurewebsites.net/pubs/chandy.pdf) | 13 | Chapter 01：Marker、Snapshot |
| `netzer-xu-1993-consistent-global-snapshots.pdf` | Netzer、Xu，1993，[Necessary and Sufficient Conditions for Consistent Global Snapshots](https://cs.brown.edu/research/pubs/techreports/reports/93/cs93-32.pdf) | 13 | Chapter 01：Z-Path、Z-Cycle |
| `lamport-2001-paxos-made-simple.pdf` | Lamport，2001，[Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) | 14 | Chapter 02：Paxos 核心與狀態機 |
| `lamport-1998-part-time-parliament.pdf` | Lamport，1998，[The Part-Time Parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) | 33 | Chapter 02：Paxos 歷史來源 |
| `fischer-lynch-paterson-1985-impossibility-of-consensus.pdf` | Fischer、Lynch、Paterson，1985，[Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf) | 9 | Chapter 02：FLP |
| `ongaro-ousterhout-2014-raft-extended.pdf` | Ongaro、Ousterhout，2014，[In Search of an Understandable Consensus Algorithm（Extended Version）](https://raft.github.io/raft.pdf) | 18 | Chapter 00／02：Raft |
| `decandia-et-al-2007-dynamo.pdf` | DeCandia 等，2007，[Dynamo: Amazon's Highly Available Key-value Store](https://cdn.amazon.science/ac/1d/eb50c4064c538c8ac440ce6a1d91/dynamo-amazons-highly-available-key-value-store.pdf) | 16 | Chapter 01：Vector Clock 的版本管理應用 |

每檔已檢查 PDF 檔頭、可開啟性、頁數與開頭頁面的題名資訊。這裡的頁數包含封面及目錄，與論文印刷頁碼可能不同；也不是課程講義 P1–P270 的引用系統。下載不代表額外完成全文研讀，筆記所用範圍仍以各章的來源說明為準。

八篇的首末頁皆可渲染。Netzer–Xu 原始檔以 pypdf 開啟時出現部分 object offset 警告，仍可讀取 13 頁；已另以 PyMuPDF 渲染並檢視首末頁，保留下載原檔與其雜湊，未重新產生或覆寫 PDF。

這些檔案供本機閱讀，未確認可公開再散布，故不加入 Git。Flink、etcd、ZooKeeper 等 HTML 官方文件保留線上引用，不另轉成論文 PDF。

### 論文來源指紋

```text
lamport-1978-time-clocks.pdf
SHA-256 c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
chandy-lamport-1985-distributed-snapshots.pdf
SHA-256 285e71bf56470620ff6080be39a416ea5de0ec855750983f50471712226b1d6a
netzer-xu-1993-consistent-global-snapshots.pdf
SHA-256 b6509c75dc8720b0dcc226f6b93fca75315c7e024a9da5e12f6c4d864dd48ba6
lamport-2001-paxos-made-simple.pdf
SHA-256 c83b5141257730d6fd20097ef17ebd02a02dfcb1809bad5873b7739659bb3f2b
lamport-1998-part-time-parliament.pdf
SHA-256 cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
fischer-lynch-paterson-1985-impossibility-of-consensus.pdf
SHA-256 80e1c33be45362d6ce0eeaba0259939df16eaff592cd612d42d783e4686c82b7
ongaro-ousterhout-2014-raft-extended.pdf
SHA-256 5a5c679b6a7c88007faeff8c3eef19a77e9e5caa8bd7390922584fe8ecf0ce1f
decandia-et-al-2007-dynamo.pdf
SHA-256 5cacd624cd7bfd37e3d22e04d8c2e347a49579d2927dbb06f40a89c0bcd40bd4
```
