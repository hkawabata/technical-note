---
title: ウェーブレット変換
---

# ウェーブレット変換とは

wavelet transform

時系列データに対して、信号の時間と周波数の関係を同時に解析するための手法。

同じく時系列データを解析する手法としてフーリエ変換があるが、フーリエ変換によるスペクトル解析では、時間方向の情報が失われてしまうため、例えば「時間が後ろになるほど周波数が高くなる」ような状況を解析することが難しい。

<img src="https://user-images.githubusercontent.com/13412823/181401297-0dd45ece-355e-4831-b176-c418c5f44c24.png" alt="" width="500">

ウェーブレット変換ではその欠点を補い、時間とともにデータの周期性が変化していく様子を捉えることができる。

# 基本的な考え方・変換手順

## ウェーブレットの生成

信号の周波数成分を解析するための物差しとして導入する「波の断片」を **ウェーブレット**と呼ぶ。  
基準となる**マザーウェーブレット**をメキシカンハット関数

$$
\psi(t) = \left(1 - t^2 \right) \exp{ \left( - \cfrac{t^2}{2} \right)}
$$

などで定義する（以後の説明では、ウェーブレットとしてメキシカンハット関数を使用）。

<img src="https://user-images.githubusercontent.com/13412823/181408870-68f10e7e-dfa2-4ef5-8b79-e28e51acec71.png" alt="" width="500">

これを時間軸方向に拡大・縮小 / 平行移動して色々な形のウェーブレットを生成し、後の変換に用いる：

$$
\psi_{\sigma, t_0}(t)
= \cfrac{1}{\sqrt{\sigma}} \psi \left( \cfrac{t-t_0}{\sigma} \right)
= \cfrac{1}{\sqrt{\sigma}} \left(1 - \cfrac{(t-t_0)^2}{\sigma^2} \right) \exp{ \left( - \cfrac{(t-t_0)^2}{2\sigma^2} \right)}
$$

| パラメータ | 説明 |
| :-- | :-- |
| $\sigma$ | 拡大縮小のパラメータ。波の波長に相当(逆数 $\frac{1}{\sigma}$ は周波数に相当) |
| $t_0$ | 平行移動のパラメータ。波の中心位置に相当 |

ここで、$\sigma$ 倍に引き伸ばされた波のエネルギーのスケールを合わせるため、重み $\frac{1}{\sqrt{\sigma}}$ をかけている。

![](https://user-images.githubusercontent.com/13412823/181709828-9fc224b4-ee70-42ba-9b95-e87b9ca75277.png)

<details>
<summary>（展開：作図に使ったコード）</summary>
{% gist 3bd481ef29271e88d567126aa0efb1b2 wavelet.py %}
</details>


## 時間・周波数的な特徴の計算

用意した色々なウェーブレット $\psi_{\sigma, t_0}(t)$ と元の時系列データ $f(t)$ とで、同じ時刻の成分どうしの積 $\psi_{\sigma, t_0}(t) f(t)$ を取り、全時間で積分することを考える。

$$
I(\sigma, t_0) = \int_{-\infty}^{\infty} \psi_{\sigma, t_0}(t) f(t) dt
$$

ウェーブレット $\psi_{\sigma, t_0}(t)$ は、以下の特徴を持つ波であると考えることができる。
- 特定の時刻 $t_0$ 付近だけに高い振幅を持つ
- 波長（周期）が $\sigma$ に比例する

なので、
- 積 $\psi_{\sigma, t_0}(t) f(t)$ の値は、時刻 $t_0$ 付近以外ではゼロに近い値になる
- その積分値 $I(\sigma, t_0)$ は、時刻 $t_0$ 付近に同じ波長・同じ位相の波が存在すると大きな値になる
	- 位相が同じでも、ウェーブレットと時系列データの波長が異なると、積分値は打ち消しあって小さくなる

時系列データに対して様々なウェーブレットをかけて積分した具体例を下図に示す。

- blue：解析対象の時系列データ $y = \sin(t^2/5) \ \ \  (0 \le t \le 20)$
- orange：ウェーブレット $y = \psi_{\sigma, t_0}(t)$
- green：時系列データとウェーブレットの積関数

![](https://user-images.githubusercontent.com/13412823/181736071-eecf5bc3-ec83-40d2-8ff6-3096580423ab.png)

<details>
<summary>（展開：作図に使ったコード）</summary>
{% gist 3bd481ef29271e88d567126aa0efb1b2 wavelet-x-timeseries.py %}
</details>

## ウェーブレット変換

もっと細かく $\sigma, t_0$ を区切って積分 $I(\sigma, t_0)$ を計算し、2次元ヒートマップを作成することで、時間とともに波長（周波数）が変化していく様子を捉えることができる。

![Figure_3](https://user-images.githubusercontent.com/13412823/181863486-16025902-d144-4ea3-ad93-c8874358de39.png)

{% gist 3bd481ef29271e88d567126aa0efb1b2 wavelet-transform.py %}
