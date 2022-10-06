# Longest-Common-Subsequence

## 開發平台
macOS Big Sur 
## 使用開發環境
Visual Studio Code (版本: 1.70.2)
## 程式功能
給定兩個序列 (或字串)，目的是找到 兩個序列連續的共同字元，稱為共同序列 (Common Subsequence)，且長度必須最長。

## 程式設計
採用動態規劃法 (Dynamic Programming) 的設計策略進行程式設計，解決 LCS 問題。

## 輸入說明:
輸入含有多組測試資料，每組測試資料 3 列，代表兩個序列。每組測試資料的第一列有 2 個 整數 m 和 n (1 < m、n <= 100)，分別代表這兩個序列的長度，0 0 代表結束。

第二、 三列分別有 m、n 個字元，字元為英文的大寫或小寫字母。

<img width="125" alt="截圖 2022-10-07 上午1 26 31" src="https://user-images.githubusercontent.com/95215851/194379248-e729c26b-03ae-46b4-ac55-0dac7f486327.png">

## 輸出說明:

對每一組測試資料，輸出 LCS 的最佳解，包含 LCS 的長度與 LCS。

<img width="214" alt="截圖 2022-10-07 上午1 26 05" src="https://user-images.githubusercontent.com/95215851/194379714-5a95c309-6bad-4c10-9b85-7b6bee3e34c2.png">


## 程式使用範例

<img width="891" alt="截圖 2022-10-07 上午1 23 20" src="https://user-images.githubusercontent.com/95215851/194378895-ccf90bf6-39c3-4475-9b4d-70a2e87a5283.png">

若輸入的字串不符合輸入的size 則會印出ERROR。

<img width="875" alt="截圖 2022-10-07 上午1 24 17" src="https://user-images.githubusercontent.com/95215851/194378992-9ad57b71-5919-443b-81ee-b390529f8d9b.png">

