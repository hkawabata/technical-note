---
title: 欠損値
---

# 欠損値

アンケートの空欄やデータ測定のミスなど、現実のデータには **欠損値** が含まれることが多い。

| サンプル番号 | 特徴量1 | 特徴量2 | 特徴量3 | 特徴量4 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 0.1 | 1 | 10 | 100 |
| 2 | 0.2 | 2 | 20 | 200 |
| 3 | 0.3 | 3 | 30 | **NaN** |
| 4 | 0.4 | **NaN** | 40 | 400 |
| 5 | 0.5 | 5 | 50 | 500 |

## 欠損値を取り除く

失うデータが大きすぎて解析の信頼性に影響が出るリスクがある。

### 欠損値を含むサンプルを取り除く

| サンプル番号 | 特徴量1 | 特徴量2 | 特徴量3 | 特徴量4 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 0.1 | 1 | 10 | 100 |
| 2 | 0.2 | 2 | 20 | 200 |
| 5 | 0.5 | 5 | 50 | 500 |


### 欠損値を含む特徴量を取り除く

| サンプル番号 | 特徴量1 | 特徴量3 |
| :-- | :-- | :-- |
| 1 | 0.1 | 10 |
| 2 | 0.2 | 20 |
| 3 | 0.3 | 30 |
| 4 | 0.4 | 40 |
| 5 | 0.5 | 50 |


## 欠損値を補完する

### 平均値代入法

欠損のないサンプルで平均値を取る。  
バイアスがかかるため推奨されない。

| サンプル番号 | 特徴量1 | 特徴量2 | 特徴量3 | 特徴量4 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 0.1 | 1 | 10 | 100 |
| 2 | 0.2 | 2 | 20 | 200 |
| 3 | 0.3 | 3 | 30 | **300** |
| 4 | 0.4 | **2.75** | 40 | 400 |
| 5 | 0.5 | 5 | 50 | 500 |

### 多重代入法

（TODO）
