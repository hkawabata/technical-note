---
title: PyAudio
---

# インストール

```bash
$ pip install pyaudio
```

以下のようなエラーが出てインストールできない場合は`brew install portaudio`を先に実行する（Mac）。

```bash
src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
```

# 使い方

## 適当な音階の音を鳴らす

```python
import pyaudio
import numpy as np
import math

CHUNK = 4096
RATE = 44100  # サンプリングレート [Hz]

def tone(freq, length, gain):
    """
    指定した周波数の定常波を作成

    Parametes
    ---------
    freq : 周波数 [Hz]
    length : 長さ [s]
    gain : 大きさ
    """
    t = np.arange(int(length * RATE)) / RATE
    return np.sin(t * float(freq) * np.pi * 2) * gain


def play_sound(output_stream, sound):
    """
    音を鳴らす
    """
    output_stream.write(sound)


# 半音上がる際の周波数変化割合
r_semitone = math.pow(2, 1.0/12)
# ドレミの周波数
scale_hz = [261.625]
for _ in range(12):
    scale_hz.append(scale_hz[-1] * r_semitone)

p = pyaudio.PyAudio()
stream_out = p.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = RATE,
    frames_per_buffer = CHUNK,
    input = True,
    output = True
)


# ドレミファソラシド
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone(scale_hz[i], 0.5, 1.0).astype(np.float32).tostring()
    play_sound(stream_out, sound)

# 小さい音で
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone(scale_hz[i], 0.5, 0.2).astype(np.float32).tostring()
    play_sound(stream_out, sound)

# 鳴らす時間を短く
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone(scale_hz[i], 0.2, 1.0).astype(np.float32).tostring()
    play_sound(stream_out, sound)

stream_out.close()
p.terminate()
```


## 入力した音声を取り込む

```python
import pyaudio
import time
import numpy as np
import math

SECONDS = 5
CHUNK = 4096
RATE = 44100  # Hz
r = math.pow(2, 1.0/12)
r12 = r * r * r * r


def play_sound(output_stream, sound):
    output_stream.write(sound)


p = pyaudio.PyAudio()
stream_in = p.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = RATE,
    frames_per_buffer = CHUNK,
    input = True,
    output = True
)
stream_out = p.open(
    format = pyaudio.paInt16,  # int だと質が悪い？ paFloat32 にするとキレイな音に
    channels = 1,
    #rate = RATE  # そのままの高さ
    rate = int(RATE*r12),  # 高くする
    #rate = int(RATE/r12),  # 低くする
    frames_per_buffer = CHUNK,
    input = True,
    output = True
)

# 一定秒数、マイク入力の音声を繰り返す
start = time.time()
while stream_in.is_active() and time.time()-start < SECONDS:
    input_ = stream_in.read(CHUNK)
    play_sound(stream_out, input_)

stream_in.stop_stream()
stream_in.close()
stream_out.stop_stream()
stream_out.close()
p.terminate()
```


## 減衰させてみる（TODO）

```python
def tone_attenuated(freq, length):
    """
    指定した周波数の定常波を作成

    Parametes
    ---------
    freq : 周波数 [Hz]
    length : 長さ [s]
    gain : 大きさ
    """
    slen = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    x = np.arange(slen)
    return np.sin(x * t) / x


for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone_attenuated(scale_hz[i], 0.5).astype(np.float32).tostring()
    play_sound(stream_out, sound)
```
