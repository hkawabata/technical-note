---
title: PyAudio
---

# インストール

```bash
$ pip install pyaudio
```

## エラー

### 'portaudio.h' file not found

以下のようなエラーが出てインストールできない場合は`brew install portaudio`を先に実行する（Mac）。

```bash
src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
```

### cdefs.h: error: Unsupported architecture

```bash
    ...
    In file included from src/_portaudiomodule.c:27:
    In file included from /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/stdio.h:64:
    In file included from /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/_stdio.h:68:
    /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include/sys/cdefs.h:807:2: error: Unsupported architecture
    #error Unsupported architecture
     ^
```

のようなエラーが出たときは環境変数を設定すれば解決した。

```bash
export ARCHFLAGS="-arch x86_64"
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

    Parameters
    ----------
    freq   : 周波数 [Hz]
    length : 長さ [s]
    gain   : 大きさ
    """
    t = np.arange(int(length * RATE)) / RATE
    return np.sin(t * float(freq) * np.pi * 2) * gain


# 半音上がる際の周波数変化割合
r_semitone = math.pow(2, 1.0/12)
# ド〜ドの12+1音階の周波数
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
    stream_out.write(sound)

# 小さい音で
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone(scale_hz[i], 0.5, 0.2).astype(np.float32).tostring()
    stream_out.write(sound)

# 鳴らす時間を短く
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    sound = tone(scale_hz[i], 0.2, 1.0).astype(np.float32).tostring()
    stream_out.write(sound)

stream_out.close()
p.terminate()
```

## 和音を鳴らす

```python
def chord(freqs, length, gain):
    """
    和音を作成
    
    Parameters
    ---------
    freqs  : 組み合わせたい周波数のリスト
    length : 長さ [s]
    gain   : 大きさ
    """
    slen = int(length * RATE)
    result = np.zeros(slen)
    for freq in freqs:
        t = float(freq) * np.pi * 2 / RATE
        result += np.sin(np.arange(slen) * t) * gain
    return result

sound = chord([scale_hz[0], scale_hz[4], scale_hz[7]], 2, 1.0).astype(np.float32).tostring()
stream_out.write(sound)
```

可視化：

```python
from matplotlib import pyplot as plt
import numpy as np

LENGTH = 1.0
t = np.arange(int(LENGTH * RATE)) / RATE

plt.title('Monophone')
plt.xlim([0, 0.015])
plt.grid()
plt.xlabel('Time [second]')
plt.ylabel('Amplitude')
plt.plot(x, tone(scale_hz[0], LENGTH, 1.0), color='blue', linewidth=1.0, label='C')
plt.plot(x, tone(scale_hz[4], LENGTH, 1.0), color='green', linewidth=1.0, label='E')
plt.plot(x, tone(scale_hz[7], LENGTH, 1.0), color='red', linewidth=1.0, label='G')
plt.legend(loc='upper right')
plt.show()

plt.title('Chord (C major = C + E + G)')
plt.xlim([0, 0.05])
plt.grid()
plt.xlabel('Time [second]')
plt.ylabel('Amplitude')
plt.plot(x, chord([scale_hz[0], scale_hz[4], scale_hz[7]], LENGTH, 1.0), color='black', linewidth=1.0)
plt.show()

plt.title('Chord (C major = C + E + G)')
plt.xlim([0, 0.5])
plt.grid()
plt.xlabel('Time [second]')
plt.ylabel('Amplitude')
plt.plot(x, chord([scale_hz[0], scale_hz[4], scale_hz[7]], LENGTH, 1.0), color='black', linewidth=0.5)
plt.show()
```

![Unknown](https://user-images.githubusercontent.com/13412823/75091648-2d8ddc00-55b3-11ea-95cc-614a8dbd2072.png)

![Unknown-1](https://user-images.githubusercontent.com/13412823/75091647-2cf54580-55b3-11ea-877e-b2af722daa0f.png)

![Unknown-2](https://user-images.githubusercontent.com/13412823/75091645-2a92eb80-55b3-11ea-892b-573d3b9cce8c.png)


## 入力した音声を取り込む

```python
import pyaudio
import numpy as np
import math

SECONDS = 10  # 録音する秒数
CHUNK = 1024  # 音源から1回読み込むときのデータサイズ
RATE = 44100  # サンプリング周波数
FORMAT = pyaudio.paInt16  # int だと質が低い？ 他に paFloat32 なども

# 半音上げるための周波数の変換倍率
R12 = math.pow(2, 1.0/12)

p = pyaudio.PyAudio()
stream_in = p.open(
    format = FORMAT,
    channels = 1,  # モノラル
    rate = RATE,
    frames_per_buffer = CHUNK,
    input = True
)
stream_out = p.open(
    format = FORMAT,
    channels = 1,
    rate = RATE,  # そのままの高さ
    #rate = int(RATE*R12),  # 高くする
    #rate = int(RATE/R12),  # 低くする
    frames_per_buffer = CHUNK,
    output = True
)

print('----- Start recording -----')

frames = []
for i in range(0, int(RATE / CHUNK * SECONDS)):
    data = stream_in.read(CHUNK, exception_on_overflow = False)
    frames.append(data)

print('----- Finish recording -----')
stream_in.stop_stream()
stream_in.close()

len(frames)
# 430
len(frames[0])
# 2048
len(np.frombuffer(frames[0], dtype=np.int16))
# 1024

result = np.frombuffer(b''.join(frames), dtype=np.int16)
len(result)
# 440320

# 取り込んだ音声を再生
stream_out.write(result.tostring())

stream_out.stop_stream()
stream_out.close()
p.terminate()
```

取り込んだ音（口笛）可視化：

```python
from matplotlib import pyplot as plt
t = np.arange(len(result)) / RATE

plt.title('Input from Microphone (ALL)')
plt.grid()
plt.xlabel('Time [second]')
plt.ylabel('Amplitude')
plt.xlim([t[0], t[-1]])
plt.plot(t, result, color='black', linewidth=0.2)
plt.show()

plt.title('Input from Microphone (Expanded)')
plt.grid()
plt.xlabel('Time [second]')
plt.ylabel('Amplitude')
plt.xlim([0.61, 0.66])
plt.plot(t, result, color='black', linewidth=0.5)
plt.show()
```

![Unknown-5](https://user-images.githubusercontent.com/13412823/75104308-231f2100-564b-11ea-8b51-521e5998644f.png)

![Unknown-6](https://user-images.githubusercontent.com/13412823/75104307-21555d80-564b-11ea-976b-e122bb6003cc.png)

ノイズらしき音：

![Unknown-7](https://user-images.githubusercontent.com/13412823/75104750-10f3b180-5650-11ea-92d5-a357587cc007.png)
