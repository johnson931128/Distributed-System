# Distributed Systems 學習筆記

將國立成功大學 Prof. Hung-Chang Hsiao 的 Distributed Systems (Fall 2026) 講義擴寫成可推演, 除錯與比較設計的工程筆記. 使用繁體中文與 American English 技術名詞; 以完整協定, 數值案例, 故障反例與附解析的英文單選題為主.

**Chapter 00–04 (P1–P117) 已完成教學改版.** 從正常案例和圖解引入機制, 再解釋故障, 正確性與限制. 使用者已確認的學習進度為 P1–P62, Chapter 03/04 已整理, 待閱讀. 下一個整理單元從 P118 開始. [筆記目錄](notes/README.md)

## 章節索引與進度

| 章節 | 合併講義實體頁碼 | GitHub 筆記 | 進度 | HackMD |
| --- | --- | --- | --- | --- |
| 00 Course Introduction | P1–P17 | [課程簡介](notes/00-course-introduction.md) | 已學習/已撰寫 | 待連結 |
| 01 Logical Clocks, Global States & Checkpointing | P18–P40 | [邏輯時鐘與回復](notes/01-logical-clocks-checkpointing.md) | 已學習/已撰寫 | 待連結 |
| 02 Fault Tolerance, Paxos & Raft | P41–P62 | [容錯與共識](notes/02-fault-tolerance-paxos-raft.md) | 已學習/已撰寫 | 待連結 |
| 03 ZooKeeper | P63–P89 | [分散式協調服務](notes/03-zookeeper.md) | 已整理/待閱讀 | 待連結 |
| 04 P2P & Gossip | P90–P117 | [P2P, Gossip 與 DHT](notes/04-peer-to-peer-gossip.md) | 已整理/待閱讀 | 待連結 |
| 05 Consistency, Replication & Transactions | P118–P155 | 規劃中 | 待學習 | 待連結 |
| 06 LevelDB & HBase | P156–P182 | 規劃中 | 待學習 | 待連結 |
| 07 HDFS, MapReduce, YARN & Spark | P183–P210 | 規劃中 | 待學習 | 待連結 |
| 08 Kafka & Stream Processing | P211–P238 | 規劃中 | 待學習 | 待連結 |
| 09 Blockchain Foundations | P239–P270 | 規劃中 | 待學習 | 待連結 |

## 教材與來源

`reference/整包.pdf` 已確認 270 頁, 章節邊界與上述頁碼相符.`reference/Distributed_Systems_4.pdf` 是 van Steen/Tanenbaum 的 *Distributed Systems* 第四版, 題名頁 Version 4.03x, 共 685 頁; 它是原理補充, 不能與講義頁碼混用. 完整身份, 版本差異, 重複內容比對與圖表核對見 [教材紀錄](reference/README.md).

兩份 PDF 由使用者保留本機; `.gitignore` 排除`reference/*.pdf`. 本專案不再散布原始教材, 不以整頁投影片或書籍圖片代替自行撰寫的說明.

主要延伸來源:

- Lamport, [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).
- Chandy, Lamport, [Distributed Snapshots](https://lamport.azurewebsites.net/pubs/chandy.pdf).
- Netzer, Xu, [Necessary and Sufficient Conditions for Consistent Global Snapshots](https://cs.brown.edu/research/pubs/techreports/reports/93/cs93-32.pdf).
- Lamport, [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf).
- Fischer, Lynch, Paterson, [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf).
- Ongaro, Ousterhout, [Raft Extended Version](https://raft.github.io/raft.pdf).
- [原文書作者頁](https://www.distributed-systems.net/index.php/books/ds4/), [Raft 資源](https://raft.github.io/), [etcd v3.6 Learner 文件](https://etcd.io/docs/v3.6/learning/design-learner/).

ZooKeeper, Gossip, CAN, Chord 與 CFS 的技術細節另參考原始論文及官方文件. 改版也對照原文書與 MIT 6.5840 的 Introduction, Raft 和 ZooKeeper 講義. 各篇章末列出使用範圍及投影片對照, 原始文獻的本機下載對照見教材紀錄. [MIT 6.5840 課程表](https://pdos.csail.mit.edu/6.824/schedule.html) · [教材紀錄](reference/README.md)

## GitHub ↔ HackMD 使用方式

GitHub 是版本控制來源, HackMD 用於閱讀, 註解與分享; 每篇 Note 對應一個`notes/*.md`, 並非自動同步整個資料夾.

1. GitHub 已有筆記時, 在 HackMD 建立空 Note, 使用 **Versions and GitHub Sync → Pull from GitHub**, 選`johnson931128/Distributed-System / main / notes/檔名.md`. 不要從空 Note Push.
2. HackMD 已有人工筆記時, 先備份/匯出, 比較內容, 再 Push 到正確 GitHub 路徑; Codex 以`git pull --ff-only` 取得後才繼續編輯.
3. Codex 修改並獲授權 push 後, 在 HackMD 手動 Pull. 不要兩邊同時修改同一篇, 遇差異先保留版本, 避免覆寫.
4. 相對章節連結服務 GitHub; HackMD 使用已知 Note URL 或 [筆記目錄中的完整 GitHub 連結](notes/README.md). Note URL 未知就寫待連結.
5. 所有公開圖片放`assets/`; 圖片 URL 使用`https://raw.githubusercontent.com/johnson931128/Distributed-System/main/assets/檔名`. 先提交到 GitHub, 再驗證外部顯示. SVG 異常時提供 PNG 備援, 來源與授權也需記錄.

目前圖表為內嵌 Mermaid, 核心說明亦保留文字. 公式統一使用 GitHub 與 HackMD 共通的 LaTeX 語法, 例如 $q=\left\lfloor\frac{N}{2}\right\rfloor+1$. 標題不使用 LaTeX.

## 驗證與後續工作

教材文字與指定圖表已核對; 本機驗證項目及實際結果記錄於 [驗證紀錄](VALIDATION.md). 本機渲染, GitHub 實際顯示, HackMD 實際顯示分開回報, 不以語法檢查代替線上驗收.

教學改版的本機檢查與雙平台驗收狀態見驗證紀錄. P118 起尚待整理.
