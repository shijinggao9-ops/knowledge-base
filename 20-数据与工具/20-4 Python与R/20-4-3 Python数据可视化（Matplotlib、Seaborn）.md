---
tags: [Python, 数据可视化, Matplotlib, Seaborn, 数据分析, 商科知识库]
date: 2026-08-05
---
**定位**：数据可视化的本质是“将数据转化为洞察”——人脑处理图像的速度比处理表格快60,000倍，一个好的图表能在一秒钟内传递核心信息。Matplotlib是Python最基础的绘图库，Seaborn是在Matplotlib基础上构建的高级统计可视化库。两者关系类似于“基础画布”和“精美模板”：Matplotlib提供最大的自由度，Seaborn提供更美观的默认样式和更简洁的API。这个文件覆盖从基础图表到高级统计图形的完整可视化流程，帮助你用Python产出可用于报告和演讲的专业图表。

**适用场景**：数据分析结果的图形化呈现、自动化报表中的图表生成、面试中的Python可视化题、学术/商业报告中的统计图形。


## 一、核心概念词典

### 1.1 Matplotlib基础

Matplotlib是Python最基础的绘图库——其他可视化库（如Seaborn）都建立在它的基础之上。

#### 画布与子图

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建画布（Figure）和坐标轴（Axes）
fig, ax = plt.subplots(figsize=(10, 6))  # 10x6英寸

# 多子图：2行2列
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot([1, 2, 3], [4, 5, 6])  # 访问第1行第1列
```
#### 常见图表类型

**折线图（plot）** ：

```python

# 月度趋势数据
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [120, 135, 148, 162, 175, 190]
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
plt.title('2026年上半年月度销售额趋势', fontsize=16)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额（万元）', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

**柱状图（bar）** ：

```python

# 各区域销售额对比
regions = ['北京', '上海', '广州', '深圳', '杭州']
sales = [250, 220, 180, 200, 150]
plt.figure(figsize=(10, 6))
plt.bar(regions, sales, color='steelblue', edgecolor='white')
plt.title('各区域销售额', fontsize=16)
plt.xlabel('区域', fontsize=12)
plt.ylabel('销售额（万元）', fontsize=12)
# 添加数值标签
for i, v in enumerate(sales):
    plt.text(i, v + 5, str(v), ha='center', fontsize=11)
plt.show()
```

**水平条形图（barh）** ：

```python

plt.figure(figsize=(10, 6))
plt.barh(regions, sales, color='steelblue')
plt.title('各区域销售额', fontsize=16)
plt.xlabel('销售额（万元）', fontsize=12)
```

**散点图（scatter）** ：

```python

# 广告费 vs 销售额
ad_spend = [10, 15, 20, 25, 30, 35, 40, 45, 50]
sales = [120, 145, 160, 185, 200, 210, 230, 255, 270]
plt.figure(figsize=(10, 6))
plt.scatter(ad_spend, sales, s=100, c='steelblue', alpha=0.7)
plt.title('广告投入与销售额关系', fontsize=16)
plt.xlabel('广告费（万元）', fontsize=12)
plt.ylabel('销售额（万元）', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

**直方图（hist）** ：

```python

# 客单价分布
prices = np.random.normal(500, 150, 1000)  # 模拟1000个客单价数据
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=30, color='steelblue', edgecolor='white', alpha=0.7)
plt.title('客单价分布', fontsize=16)
plt.xlabel('客单价（元）', fontsize=12)
plt.ylabel('订单数', fontsize=12)
plt.axvline(prices.mean(), color='red', linestyle='--', linewidth=2, label=f'均值：{prices.mean():.0f}元')
plt.legend()
plt.show()
```

**饼图（pie）** ：

```python

# 各产品线收入占比
products = ['电子产品', '服装', '食品', '家居', '其他']
revenue = [380, 220, 180, 120, 100]
plt.figure(figsize=(8, 8))
plt.pie(revenue, labels=products, autopct='%1.1f%%', startangle=90)
plt.title('各产品线收入占比', fontsize=16)
plt.show()
```

**箱线图（boxplot）** ：

```python

# 各区域客单价分布对比
data_by_region = [
    [320, 450, 380, 520, 410],  # 北京
    [280, 350, 420, 390, 360],  # 上海
    [200, 310, 280, 350, 300],  # 广州
]
plt.figure(figsize=(10, 6))
plt.boxplot(data_by_region, labels=['北京', '上海', '广州'])
plt.title('各区域客单价分布对比', fontsize=16)
plt.ylabel('客单价（元）', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.show()
```
### 1.2 图表美化技巧

```python

# 设置全局样式（中文字体支持）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 颜色选择
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']
plt.bar(x, y, color=colors)
# 图例
plt.plot(x1, y1, label='2025年')
plt.plot(x2, y2, label='2026年')
plt.legend(loc='upper left')  # 位置：upper left / lower right / best
# 多图叠加
plt.figure(figsize=(12, 6))
plt.plot(months, sales_2025, label='2025年', marker='o')
plt.plot(months, sales_2026, label='2026年', marker='s')
plt.fill_between(months, sales_2025, sales_2026, alpha=0.2)  # 填充区域
plt.legend()
plt.show()
```

### 1.3 Seaborn概览

Seaborn是基于Matplotlib构建的高级可视化库，提供了更美观的默认样式和专门针对统计分析设计的图表类型。

#### Seaborn vs Matplotlib

|维度|Matplotlib|Seaborn|
|---|---|---|
|设计哲学|高度可定制，自由度最高|统计可视化，优雅默认样式|
|代码量|较多（需手动设置很多细节）|较少（多数细节自动处理）|
|统计图表|需手动计算|内置统计计算|
|数据格式|接受列表/数组|原生支持DataFrame|
|学习曲线|较陡|较平缓|

**安装与导入**：

```python

import seaborn as sns
import matplotlib.pyplot as plt
# 设置Seaborn主题
sns.set_theme(style='whitegrid')  # 白底网格
sns.set_palette('deep')           # 配色方案
```

#### Seaborn核心图表

**分类统计图（barplot / countplot）** ：

```python

import pandas as pd
# 模拟数据
data = pd.DataFrame({
    '城市': ['北京', '上海', '北京', '广州', '上海', '北京', '深圳', '广州'],
    '销售额': [25000, 18000, 32000, 15000, 21000, 28000, 19000, 16000]
})
# 柱状图（自动计算均值并显示置信区间）
sns.barplot(data=data, x='城市', y='销售额')
plt.title('各城市平均销售额', fontsize=16)
plt.show()
# 计数图（统计各分类的出现次数）
sns.countplot(data=data, x='城市')
```

**箱线图（boxplot）** ：

```python

# 使用Seaborn的boxplot，自动按分类分组
sns.boxplot(data=data, x='城市', y='销售额')
plt.title('各城市销售额分布', fontsize=16)
plt.show()
```

**小提琴图（violinplot）** ——箱线图的升级版，同时显示分布形态：

```python

sns.violinplot(data=data, x='城市', y='销售额')
plt.title('各城市销售额分布（小提琴图）', fontsize=16)
plt.show()
```

**分布图（histplot / kdeplot）** ：

```python

# 直方图 + 密度曲线
sns.histplot(data=df, x='客单价', kde=True, bins=30)
plt.title('客单价分布', fontsize=16)
# 仅密度曲线
sns.kdeplot(data=df, x='客单价', fill=True)
# 多组对比
sns.kdeplot(data=df, x='客单价', hue='城市', fill=True, alpha=0.3)
```

**关系图（scatterplot / pairplot）** ：

```python

# 散点图 + 回归线
sns.regplot(data=df, x='广告费', y='销售额')
plt.title('广告费与销售额关系', fontsize=16)
# 多变量成对关系矩阵
sns.pairplot(df[['销售额', '订单数', '客单价', '广告费']])
plt.show()
```

**热力图（heatmap）——相关性分析最常用** ：

```python

# 计算相关系数矩阵
corr = df[['销售额', '订单数', '客单价', '广告费']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
plt.title('变量相关性热力图', fontsize=16)
plt.show()
```
 
**分类图（catplot）** ——Seaborn最强大的分类可视化函数，整合了多种分类图表类型：

```python

# 使用catplot可以快速切换图表类型
sns.catplot(data=df, x='城市', y='销售额', kind='box')      # 箱线图
sns.catplot(data=df, x='城市', y='销售额', kind='violin')   # 小提琴图
sns.catplot(data=df, x='城市', y='销售额', kind='bar')      # 柱状图
```

### 1.4 图表保存

```python

# 保存为图片（用于报告、PPT、邮件）
plt.savefig('sales_chart.png', dpi=300, bbox_inches='tight')
# 保存为高清矢量图（适合印刷）
plt.savefig('sales_chart.pdf', bbox_inches='tight')
```

## 二、商业场景还原

### 场景1：销售月度趋势分析（Matplotlib折线图）

**情境**：需要向管理层汇报2026年上半年销售趋势，展示月度变化和增长态势。

```python

import matplotlib.pyplot as plt
import pandas as pd
# 数据
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [1250, 1320, 1480, 1560, 1720, 1890]
plt.figure(figsize=(12, 6))
plt.plot(months, sales, marker='o', linewidth=3, markersize=10, color='#2E86AB')
plt.fill_between(months, sales, alpha=0.2, color='#2E86AB')
# 添加数据标签
for i, v in enumerate(sales):
    plt.text(i, v + 30, f'{v}万', ha='center', fontsize=11, fontweight='bold')
plt.title('2026年上半年销售额趋势', fontsize=18, fontweight='bold')
plt.xlabel('月份', fontsize=14)
plt.ylabel('销售额（万元）', fontsize=14)
plt.grid(True, alpha=0.3)
# 在图上标注增长
plt.annotate('增长51%', xy=(5, 1890), xytext=(4, 2000),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')
plt.tight_layout()
plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 场景2：各城市销售额对比（Seaborn柱状图）

**情境**：需要对比各城市销售表现，并同时显示每个城市的销售分布情况。

```python

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 模拟数据：每个城市多笔销售记录
np.random.seed(42)
cities = ['北京', '上海', '广州', '深圳', '杭州']
data = pd.DataFrame({
    '城市': np.repeat(cities, 50),
    '销售额': np.concatenate([
        np.random.normal(28000, 5000, 50),
        np.random.normal(24000, 4500, 50),
        np.random.normal(20000, 4000, 50),
        np.random.normal(22000, 4800, 50),
        np.random.normal(18000, 3500, 50)
    ])
})
# 设置样式
sns.set_theme(style='whitegrid')
plt.figure(figsize=(12, 6))
# 同时展示箱线图和小提琴图
ax = sns.boxplot(data=data, x='城市', y='销售额', palette='Set2')
sns.swarmplot(data=data, x='城市', y='销售额', color='black', alpha=0.3, size=4)
plt.title('各城市销售额分布对比', fontsize=16, fontweight='bold')
plt.xlabel('城市', fontsize=14)
plt.ylabel('销售额（元）', fontsize=14)
plt.xticks(fontsize=12)
plt.tight_layout()
plt.show()
```

### 场景3：相关性热力图（Seaborn heatmap）

**情境**：分析销售额、订单数、客单价、广告费、客户数之间的相关性，找出影响销售额的关键因素。

```python

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 模拟数据
np.random.seed(42)
n = 100
df = pd.DataFrame({
    '销售额': np.random.normal(1000, 200, n),
    '订单数': np.random.normal(80, 15, n),
    '客单价': np.random.normal(500, 100, n),
    '广告费': np.random.normal(50, 15, n),
    '客户数': np.random.normal(200, 40, n)
})
# 计算相关系数矩阵
corr = df.corr()
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))  # 只显示下三角
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={'shrink': 0.8}
)
plt.title('核心指标相关性热力图', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 场景4：多变量关系探索（Pairplot）

**情境**：探索不同城市下，销售额与客单价、订单数之间的多维关系。

```python

# 添加城市标签
df['城市'] = np.random.choice(['北京', '上海', '深圳'], n)
sns.pairplot(
    df,
    vars=['销售额', '客单价', '订单数', '广告费'],
    hue='城市',
    diag_kind='kde',
    plot_kws={'alpha': 0.6},
    height=2.5
)
plt.suptitle('各城市多维指标关系矩阵', fontsize=16, y=1.02)
plt.show()
```

## 三、面试高频题

### 3.1 代码题

**题目1：用Matplotlib画一张折线图，展示2026年1-12月的销售趋势。**

```python

import matplotlib.pyplot as plt
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
sales = [120, 135, 148, 162, 175, 190, 195, 188, 176, 182, 195, 210]
plt.figure(figsize=(12, 6))
plt.plot(months, sales, marker='o', linewidth=2)
plt.title('2026年销售趋势')
plt.xlabel('月份')
plt.ylabel('销售额（万元）')
plt.grid(True, alpha=0.3)
plt.show()
```

**题目2：用Seaborn画一张热力图，展示变量之间的相关性。**

```python

import seaborn as sns
import matplotlib.pyplot as plt
# df是一个包含多个数值列的DataFrame
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()
```

### 3.2 常见面试追问

|追问|回答要点|
|---|---|
|"Matplotlib和Seaborn有什么区别？"|Matplotlib是基础库，高度可定制；Seaborn是高级库，默认更美观，与DataFrame集成更好|
|"什么时候用折线图，什么时候用柱状图？"|折线图展示趋势（时间序列），柱状图展示对比（类别之间）|
|"如何在一张图上叠加多条折线？"|使用两次`plt.plot()`，然后用`plt.legend()`添加图例|

## 四、常见错误与陷阱

|错误|后果|正确做法|
|---|---|---|
|忘记导入`matplotlib.pyplot`|`NameError`|`import matplotlib.pyplot as plt`|
|中文显示为方块|图表无法阅读|设置中文字体：`plt.rcParams['font.sans-serif'] = ['SimHei']`|
|`plt.show()`和`plt.savefig()`顺序错误|保存的图片为空白|先`savefig`后`show`|
|颜色过多|视觉杂乱|控制在5种以内，使用颜色调色板|
|`sns.pairplot`在大数据集上运行很慢|等待时间过长|抽样数据后再绘图：`df.sample(500)`|

## 五、实战自测题

- [ ] **折线图**：用Matplotlib画出2026年1-12月的销售额趋势，并标注最高点和最低点。
    
- [ ] **柱状图**：用Seaborn画出各产品的销售额对比柱状图，并添加误差线（置信区间）。
    
- [ ] **热力图**：用Seaborn画出`df[['销售额','订单数','客单价','客户数','广告费']]`的相关性热力图。
    
- [ ] **散点图**：用Seaborn的`regplot`画出广告费和销售额的关系，并添加回归线。
    
- [ ] **综合题**：从Excel读取数据 → 用Pandas做分组汇总 → 用Matplotlib画出汇总结果的柱状图 → 保存为PNG文件。

## 六、关联笔记

- [[20-4-1 Python基础语法与数据环境搭建]]（环境搭建与基础语法）
- [[20-4-2 Python数据分析核心库（Pandas、NumPy）]]（可视化所使用的数据来源）
- [[20-3-3 可视化图表与仪表板设计]]（图表选择与设计原则）
- [[30-2-3 PPT的视觉呈现与数据可视化]]（图表在商业报告中的应用）
- [[85-7 数据分析]]（Python可视化在数据分析岗位中的应用）