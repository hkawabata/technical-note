---
title: TD 法
title-en: TD-Learning
---
# TD 法とは

**TD 法（Temporal Difference Learning）** は、モデルフリーの強化学習手法の1つ。

# 理論（考え方）

各状態 $s$ の価値評価の見積もりを $V(s)$ とする。
ここから行動 $a$ を取った結果、報酬 $r$ を得て状態 $s'$ に遷移したとすると、