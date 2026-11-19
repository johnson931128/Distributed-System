# 筆記驗證紀錄

日期：2026-11-19。範圍為講義 P1–P62 的三章筆記及其索引、規範、來源紀錄。**撰寫完成、本機驗證、線上雙平台驗收是三個不同狀態。**

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
