---
title: datetime
---
# 概要

日付・時刻関係を取り扱う標準ライブラリ。
日付・時刻を `datetime.datetime` オブジェクトとして取り扱う
# 使い方

## datetime: 日付・時刻のオブジェクト

### コンストラクタで生成

```python
from datetime import datetime, date, time

dt_ymd = datetime(2020, 10, 1)
dt_ymdHMS = datetime(2020, 10, 1, 15, 20, 10)
dt_ymdHMSmicroS = datetime(2020, 10, 1, 15, 20, 10, 123456)
print(dt_ymd)
# 2020-10-01 00:00:00
print(dt_ymdHMS)
# 2020-10-01 15:20:10
print(dt_ymdHMSmicroS)
# 2020-10-01 15:20:10.123456

d_ymd = date(2020, 10, 1)
print(d_ymd)
# 2020-10-01

t_H = time(15)
t_HM = time(15, 21)
t_HMS = time(15, 21, 10)
t_HMSmicroS = time(15, 21, 10, 123456)
print(t_H)
# 15:00:00
print(t_HM)
# 15:21:00
print(t_HMS)
# 15:21:10
print(t_HMSmicroS)
# 15:21:10.123456
```

### 現在の日付・時刻を取得

```python
d_today = date.today()
# datetime.date(2023, 12, 8)
dt_now = datetime.now()
# datetime.datetime(2023, 12, 8, 13, 25, 29, 630801)

print(d_today)
# 2023-12-08
print(dt_now)
# 2023-12-08 13:25:29.630801
```

※ `datetime` ではなく `time` モジュールを使えば、現在時刻を unix time で取得できる。

```python
import time

ut = time.time()
# 1702015381.590993
```

### 文字列をパースして取得

```python
# 値, 書式の順に指定
ymd = datetime.strptime('2023-10-01', '%Y-%m-%d')
ymd_hms = datetime.strptime('2023/10/01 12:34:56', '%Y/%m/%d %H:%M:%S')
```


### 書式を指定して文字列に変換

```python
dt = datetime.now()
# datetime.datetime(2023, 12, 10, 9, 10, 39, 145502)
dt_str = dt.strftime('%Y/%m/%d-%H:%M:%S.%f')
# 2023/12/10-09:10:39.145502
```

## timedelta: 日時の差のオブジェクト

日時の差は `datetime.timedelta` オブジェクトで表される。

### コンストラクタで生成

```python
from datetime import datetime, timedelta

"""
コンストラクタ：
timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
"""
delta_t = timedelta(days=1, hours=6, minutes=10, seconds=3)
# datetime.timedelta(days=1, seconds=22203)
print(delta_t)
# 1 day, 6:10:03
```

### datetime の差を計算して取得

```python
dt1 = datetime(2020, 10, 1, 15, 20, 10)
dt2 = datetime(2021, 11, 2, 16, 21, 11)
delta_t = dt2 - dt1
# datetime.timedelta(days=397, seconds=3661)

delta_t.days            # 397
delta_t.seconds         # 3661
delta_t.microseconds    # 0
delta_t.total_seconds() # 34304461.0
print(delta_t)
# 397 days, 1:01:01
```

### timedelta を使った日時の足し引き

```python
dt_start = datetime.strptime('2023-10-01', '%Y-%m-%d')
delta_t = timedelta(days=1)
for n in range(7):
    print(dt_start + n*delta_t)

"""
2023-10-01 00:00:00
2023-10-02 00:00:00
2023-10-03 00:00:00
2023-10-04 00:00:00
2023-10-05 00:00:00
2023-10-06 00:00:00
2023-10-07 00:00:00
"""
```
