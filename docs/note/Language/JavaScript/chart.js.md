---
title: Chart.js
---

# Chart.js とは

種々のグラフ・チャートを描画するためのライブラリ

# 基本的な使い方

```html
<html>
  <head>
    <meta charset="UTF-8">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
  </head>
  <body>
    <!-- 描画エリア -->
    <canvas id="myChart" ></canvas>
    <!-- グラフ内容を記述 -->
    <script>
      var ctx = document.getElementById('myChart');
      var x = [1, 2, 3, 4, 5, 6];
      var y1 = [100, 121, 187, 169, 224, 240];
      var y2 = [100, 152, 120, 178, 265, 197];
      var myChart = new Chart(ctx, {
        type: 'line',  // 折れ線グラフ
        data: {
          labels: x,  // 横軸の値
          datasets: [{
            label: 'A',
            data: y1
          },
          {
            label: 'B',
            data: y2
          }]
        },
        options: {
          title: {
            display: true,
            text: 'Title of Chart',
            fontSize: 20
          },
          legend: {
            display: true  // 凡例を表示する
          },
          scales: {
            // X軸
            xAxes: [{
              // 軸ラベル表示
              scaleLabel: {
                display: true,
                labelString: 'Month'
              },
              // X軸の範囲を指定
              ticks: {
                min: 0,
                max: 8
              }
            }],
            yAxes: [{
              // 軸ラベル表示
              scaleLabel: {
                display: true,
                labelString: 'Price'
              },
              // Y軸の範囲を指定
              ticks: {
                min: 0,
                max: 300
              }
            }]
          }
        }
      });
    </script>
  </body>
</html>
```

