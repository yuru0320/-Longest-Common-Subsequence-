# Longest-Common-Subsequence

## 開發平台
macOS Big Sur 
## 使用開發環境
Xcode v12.5.1 (12E507) 
## 程式功能
給定兩個序列 (或字串)，目的是找到 兩個序列連續的共同字元，稱為共同序列 (Common Subsequence)，且長度必須最長。

## 程式設計
採用動態規劃法 (Dynamic Programming) 的設計策略進行程式設計，解決 LCS 問題。

## 輸入說明:
輸入含有多組測試資料，每組測試資料 3 列，代表兩個序列。每組測試資料的第一列有 2 個 整數 m 和 n (1 < m、n <= 100)，分別代表這兩個序列的長度，0 0 代表結束。
輸入範例:
76
A BC B D A B BD C A BA 76
BC D AA C D A C D BA C 00

第二、 三列分別有 m、n 個字元，字元為英文的大寫或小寫字母。

## 輸出說明:
對每一組測試資料，輸出 LCS 的最佳解，包含 LCS 的長度與 LCS。
