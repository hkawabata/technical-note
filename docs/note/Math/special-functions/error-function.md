---
title: 誤差関数
title-en: Error Function
---

# 定義

$$
\mathrm{erf}(x) = \cfrac{2}{\sqrt{\pi}}
\int_0^x e^{-t^2} dt
$$

# 正規分布との関係

正規分布の累積密度関数

$$
\Phi(x) = \cfrac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-t^2/2} dt
$$

は誤差関数を用いて表せる：

$$
\Phi(x) = \cfrac{1}{2} \left( 1 + \mathrm{erf} \left( \cfrac{x}{\sqrt{2}} \right) \right)
$$

# 計算方法

$x$ が小さいときはテイラー展開が有効：

$$
\mathrm{erf}(x) =
\cfrac{2}{\sqrt\pi}
\sum_{n=0}^\infty \cfrac{(-1)^n x^{2n+1}}{(2n+1)n!}
$$

$x$ が大きいときは連分数展開が有効：

$$
\mathrm{erf}(x) =
1 - \sqrt{\cfrac{2}{\pi}}
\cdot
\cfrac{
	e^{-x^2}
}{
	\sqrt{2} x + \cfrac{1}{
		\sqrt{2} x + \cfrac{2}{
			\sqrt{2} x + \cfrac{3}{
				\sqrt{2} x + \cfrac{4}{
					\sqrt{2} x + \cdots
				}
			}
		}
	}
}
$$

{% gist b4c458591e0585cc87877b35ec386dc8 20230701_erf.py %}

![erf](https://user-images.githubusercontent.com/13412823/250328734-9765444b-f445-4ef7-b835-8494db864b0e.png)

