---
tags: [Python, Pandas, NumPy, 数据分析, 数据处理, 商科知识库]
date: 2026-08-05
---

# 20-4-2 Python数据分析核心库（Pandas、NumPy）

**定位**：NumPy和Pandas是Python数据分析的"基础设施"——NumPy提供了高效的数组运算，Pandas在此基础上构建了DataFrame（二维表格），让Python能够处理Excel和SQL中的所有表格操作，且能应对百万级以上的数据量。这个文件覆盖Pandas中最核心的操作：数据导入、查看、筛选、清洗、分组、合并。掌握这些，你就能用Python完成日常工作中80%的数据处理任务——从多表合并到复杂分组汇总，从数据清洗到自动化报表生成。

**适用场景**：批量处理多个Excel/CSV文件、数据量大到Excel无法打开时的分析、复杂的数据清洗逻辑（如多条件筛选、多表关联）、自动化报表生成、面试中的Python数据分析题。


## 一、核心概念词典

### 1.1 NumPy基础

NumPy（Numerical Python）是Pandas的底层基础——它提供了高效的数组（`ndarray`）运算能力。虽然日常数据分析更多使用Pandas，但理解NumPy能帮你更好地理解Pandas的性能优势。

**创建NumPy数组**：

```python
import numpy as np

# 从列表创建
arr1 = np.array([1, 2, 3, 4, 5])

# 创建全0数组（5行2列）
zeros = np.zeros((5, 2))

# 创建连续整数序列（0到9）
range_arr = np.arange(10)

# 创建等间隔序列（0到1，共5个点）
linspace_arr = np.linspace(0, 1, 5)
```
**向量化运算**（NumPy的核心优势）：

```python

# 传统Python列表：需要循环
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
# NumPy：直接对整个数组做运算（速度快10-100倍）
arr = np.array([1, 2, 3, 4, 5])
squared_arr = arr ** 2        # 每个元素平方
sqrt_arr = np.sqrt(arr)       # 每个元素开方
sum_arr = arr.sum()           # 求和
mean_arr = arr.mean()         # 平均值
```

### 1.2 Pandas核心数据结构

**Series（一维数据）** ：

```python

import pandas as pd
# 从列表创建Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s['b'])  # 20
```
**DataFrame（二维表格）** ：

DataFrame是Pandas最核心的数据结构——你可以把它理解为"Python版的Excel工作表"或"内存中的SQL表"。

```python

# 从字典创建DataFrame
data = {
    '客户': ['张三', '李四', '王五', '赵六'],
    '城市': ['北京', '上海', '北京', '深圳'],
    '销售额': [25000, 18000, 32000, 15000],
    '订单数': [15, 12, 20, 8]
}
df = pd.DataFrame(data)
print(df)

#    客户  城市   销售额  订单数
# 0  张三  北京  25000   15
# 1  李四  上海  18000   12
# 2  王五  北京  32000   20
# 3  赵六  深圳  15000    8
```

### 1.3 数据导入与导出

```python

# 从CSV导入
df = pd.read_csv('sales_data.csv', encoding='utf-8')
# 从Excel导入（需要安装openpyxl）
df = pd.read_excel('sales_data.xlsx', sheet_name='2026年')
# 导出到CSV
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
# 导出到Excel
df.to_excel('output.xlsx', index=False, sheet_name='汇总')
# 从剪贴板读取（快速从Excel复制数据）
# df = pd.read_clipboard()
```

### 1.4 数据查看与探索

```python

# 查看前5行
df.head()
# 查看后5行
df.tail()
# 查看数据概览（行数、列数、每列数据类型、非空值数量）
df.info()
# 查看统计摘要（数值列的均值、标准差、分位数等）
df.describe()
# 查看行列数
df.shape          # (100, 5) 表示100行5列
# 查看列名
df.columns
# 查看索引
df.index
# 查看数据类型的快速概览
df.dtypes
```

### 1.5 数据选取与筛选

#### 基础列选择

```python

# 选择单列（返回Series）
df['客户']
# 选择多列（返回DataFrame）
df[['客户', '销售额']]
# 使用列名快捷访问（仅当列名是合法Python变量名时可用）
df.客户  # 等同于 df['客户']
```
#### loc 与 iloc

|方法|说明|示例|
|---|---|---|
|`loc[]`|按**标签**（行索引名/列名）选取|`df.loc[0:2, '客户':'销售额']`|
|`iloc[]`|按**位置**（行号/列号，从0开始）选取|`df.iloc[0:2, 0:3]`|

```python

# loc示例：按行标签和列名选取
df.loc[0:2, ['客户', '销售额']]   # 选0到2行（含2），客户和销售额列
# iloc示例：按行列位置选取
df.iloc[0:2, 0:2]                # 选前2行前2列（不含2）
```

#### 条件筛选

```python

# 单条件：销售额大于20000的客户
df[df['销售额'] > 20000]
# 多条件（且）：北京地区且销售额大于20000
df[(df['城市'] == '北京') & (df['销售额'] > 20000)]
# 多条件（或）：北京或上海的客户
df[(df['城市'] == '北京') | (df['城市'] == '上海')]
# 使用 isin() 筛选多个值
df[df['城市'].isin(['北京', '上海', '深圳'])]
# 字符串筛选：姓名包含"张"的客户
df[df['客户'].str.contains('张')]
```

#### 查询函数（更简洁的写法）

```python

# query() 可以用类SQL语法筛选
df.query("城市 == '北京' and 销售额 > 20000")
# 变量传入
city = '北京'
df.query("城市 == @city")
```

### 1.6 数据清洗

#### 空值处理

```python

# 查看每列空值数量
df.isnull().sum()
# 删除有空值的行
df.dropna()
# 删除某列有空值的行
df.dropna(subset=['客户'])
# 填充空值
df['销售额'].fillna(0)                    # 用0填充
df['销售额'].fillna(df['销售额'].mean())   # 用平均值填充
df['城市'].fillna('未知')                  # 用指定文本填充
```
#### 重复值处理

```python

# 查看重复行
df.duplicated()
# 删除重复行（保留第一个）
df.drop_duplicates()
# 按指定列去重
df.drop_duplicates(subset=['客户'])
# 保留最后一个重复项
df.drop_duplicates(keep='last')
```

#### 数据类型转换

```python

# 查看数据类型
df.dtypes
# 转换类型
df['销售额'] = df['销售额'].astype('float')
df['日期'] = pd.to_datetime(df['日期'])
```

#### 文本处理（str访问器）

```python

# 去除首尾空格
df['客户'] = df['客户'].str.strip()
# 提取包含"科技"的客户
df[df['客户'].str.contains('科技')]
# 替换文本
df['城市'] = df['城市'].str.replace('北京市', '北京')
```

### 1.7 分组聚合（Group By）

`groupby()`是Pandas中最强大的分析功能——相当于Excel中的数据透视表。

```python

# 按城市分组，计算销售额总和
df.groupby('城市')['销售额'].sum()
# 按城市分组，计算多个指标
df.groupby('城市')['销售额'].agg(['sum', 'mean', 'count', 'max'])
# 按多列分组
df.groupby(['城市', '产品类别'])['销售额'].sum()
# 使用自定义聚合函数名
df.groupby('城市').agg(
    总销售额=('销售额', 'sum'),
    平均销售额=('销售额', 'mean'),
    客户数=('客户', 'count')
)
```

#### 数据透视表（pivot_table）

```python

# 按城市和产品类别交叉汇总
pd.pivot_table(
    df,
    values='销售额',
    index='城市',        # 行
    columns='产品类别',   # 列
    aggfunc='sum'
)
# 指定多个汇总方式
pd.pivot_table(
    df,
    values='销售额',
    index='城市',
    columns='产品类别',
    aggfunc=['sum', 'mean']
)
```

### 1.8 数据合并

#### 合并（merge）——类似SQL的JOIN

```python

# 订单表和客户表合并（内连接）
merged_df = pd.merge(
    orders_df,              # 左表
    customers_df,           # 右表
    on='customer_id',       # 连接字段
    how='inner'             # inner/left/right/outer
)
# 多条件连接
pd.merge(df1, df2, on=['key1', 'key2'])
```

#### 拼接（concat）——类似SQL的UNION

```python

# 纵向拼接（行数增加）
df_combined = pd.concat([df1, df2], ignore_index=True)
# 横向拼接（列数增加）
df_combined = pd.concat([df1, df2], axis=1)
```

### 1.9 日期处理

```python

# 转换为日期类型
df['日期'] = pd.to_datetime(df['日期'])
# 提取年月日
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
df['日'] = df['日期'].dt.day
# 提取季度
df['季度'] = df['日期'].dt.quarter
# 提取星期几（0=周一）
df['星期'] = df['日期'].dt.weekday
# 筛选特定月份
df[df['日期'].dt.month == 8]
# 筛选日期范围
df[(df['日期'] >= '2026-01-01') & (df['日期'] <= '2026-06-30')]
```
### 1.10 应用函数（apply / map）

当需要对数据行进行自定义计算时，使用`apply()`。

```python

# 对销售额列应用函数
df['销售额_万元'] = df['销售额'].apply(lambda x: x / 10000)
# 对每行应用函数（axis=1表示行）
df['等级'] = df.apply(
    lambda row: '高' if row['销售额'] > 20000 else '低',
    axis=1
)
# map：将值映射为另一个值
df['城市代码'] = df['城市'].map({'北京': 'BJ', '上海': 'SH', '深圳': 'SZ'})
```

## 二、商业场景还原

### 场景1：合并多个月度销售Excel文件

**情境**：每个月收到一份销售报表（`sales_202601.csv`、`sales_202602.csv`……`sales_202612.csv`），需要合并为一张总表。


```python

import pandas as pd
import glob
# 匹配所有月度文件
file_pattern = 'sales_2026*.csv'
all_files = glob.glob(file_pattern)
# 逐个读取并合并
df_list = []
for file in all_files:
    df = pd.read_csv(file, encoding='utf-8')
    df_list.append(df)
# 纵向拼接所有数据
df_all = pd.concat(df_list, ignore_index=True)
print(f"合并完成，共 {len(df_all)} 行")
```

### 场景2：客户价值分析与分层

**情境**：有一张订单表（订单ID、客户ID、订单日期、金额），需要按客户汇总并分层。

python

# 读取数据
orders = pd.read_excel('orders.xlsx')
# 按客户汇总
customer_summary = orders.groupby('客户ID').agg(
    订单数=('订单ID', 'count'),
    总消费额=('金额', 'sum'),
    平均客单价=('金额', 'mean'),
    最近下单日=('订单日期', 'max')
).reset_index()
# 计算分层
def customer_tier(row):
    if row['总消费额'] > 100000:
        return 'VIP'
    elif row['总消费额'] > 30000:
        return '高价值'
    elif row['订单数'] > 5:
        return '活跃'
    else:
        return '普通'
customer_summary['客户分层'] = customer_summary.apply(customer_tier, axis=1)
# 分层统计
tier_stats = customer_summary.groupby('客户分层').agg(
    客户数=('客户ID', 'count'),
    总消费=('总消费额', 'sum')
)
print(tier_stats)

### 场景3：多表关联分析（订单+产品+客户）

**情境**：有三张表——订单表、产品表、客户表，需要分析各城市各品类销售额。

python

# 导入三张表
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
# 先关联订单和产品（获取产品品类）
df = pd.merge(orders, products, on='产品ID', how='left')
# 再关联客户（获取城市信息）
df = pd.merge(df, customers, on='客户ID', how='left')
# 计算金额（如果只有数量，没有金额）
df['销售额'] = df['数量'] * df['单价']
# 分组汇总：按城市×品类
result = df.groupby(['城市', '品类']).agg(
    总销售额=('销售额', 'sum'),
    订单数=('订单ID', 'nunique')
).reset_index()
# 保存结果
result.to_excel('城市_品类_分析.xlsx', index=False)

### 场景4：数据质量检查

**情境**：收到一份业务数据，需要快速检查数据质量。

python

def data_quality_report(df):
    print("=" * 50)
    print("数据质量报告")
    print("=" * 50)
    print(f"总行数：{len(df)}")
    print(f"总列数：{len(df.columns)}")
    print("\n空值情况：")
    print(df.isnull().sum())
    print("\n重复行数：")
    print(df.duplicated().sum())
    print("\n数据类型：")
    print(df.dtypes)
    print("\n数值列统计摘要：")
    print(df.describe())
# 使用
df = pd.read_excel('raw_data.xlsx')
data_quality_report(df)

## 三、面试高频题

### 3.1 基础操作题

**题目1：如何筛选DataFrame中某列大于100的行？**

python

df[df['列名'] > 100]

**题目2：如何按某列分组并计算另一列的平均值？**

python

df.groupby('分组列')['数值列'].mean()

**题目3：如何处理缺失值？**

python

# 删除
df.dropna()
# 填充
df.fillna(value)

**题目4：如何合并两张表？**

python

# 类似SQL JOIN
pd.merge(df1, df2, on='key', how='left')
# 纵向拼接
pd.concat([df1, df2], ignore_index=True)

### 3.2 综合题

**题目："请用Pandas实现：从Excel读取订单数据，按客户汇总订单数、总金额、平均金额，然后将结果导出为新Excel文件。"**

python

import pandas as pd
# 读取数据
df = pd.read_excel('orders.xlsx')
# 分组汇总
result = df.groupby('客户ID').agg(
    订单数=('订单ID', 'count'),
    总金额=('金额', 'sum'),
    平均金额=('金额', 'mean')
).reset_index()
# 导出
result.to_excel('customer_summary.xlsx', index=False)

## 四、常见错误与陷阱

|错误|后果|正确做法|
|---|---|---|
|链式索引赋值（如`df[df['A']>1]['B']=5`）|触发`SettingWithCopyWarning`，赋值可能无效|用`.loc`：`df.loc[df['A']>1, 'B'] = 5`|
|忘记在`groupby`后使用`reset_index()`|分组结果以索引形式存在，访问不变|添加`.reset_index()`|
|默认`read_csv`不指定编码|中文乱码|指定`encoding='utf-8'`或`'gbk'`|
|在循环中逐行修改DataFrame|极慢（Pandas的向量化能力未被利用）|使用向量化操作、`apply()`或列表推导式|
|不区分`loc`和`iloc`|用`iloc`时传入列名会报错|`loc`用标签，`iloc`用位置索引|
|`inplace=True`使用不当|容易产生混淆，且某些操作不支持|优先使用赋值返回新对象：`df = df.drop_duplicates()`|

## 五、实战自测题

- □ 
    
    **数据导入与查看**：读取一份CSV文件（`sales.csv`），查看前5行、数据类型、统计摘要。
    
- □ 
    
    **数据筛选**：筛选出"销售额 > 5000"且"城市 = '上海'"的订单。
    
- □ 
    
    **分组聚合**：按"产品类别"分组，计算销售额总和、平均值、订单数。
    
- □ 
    
    **数据透视表**：创建一张透视表，行=城市，列=产品类别，值=销售额总和。
    
- □ 
    
    **合并练习**：将订单表（`订单ID`、`客户ID`、`金额`）和客户表（`客户ID`、`客户名`、`城市`）合并，生成包含客户名和城市的订单明细。
    

## 六、关联笔记

- [[20-4-1 Python基础语法与数据环境搭建]]（学习Pandas前需掌握的Python基础）
    
- [[20-4-3 Python数据可视化（Matplotlib、Seaborn）]]（数据分析后的可视化呈现）
    
- [[20-2 SQL]]（Pandas的`merge`对应SQL的`JOIN`，`groupby`对应SQL的`GROUP BY`）
    
- [[20-1 Excel]]（Pandas的`pivot_table`对应Excel的数据透视表）
    
- [[85-7 数据分析]]（Pandas在数据分析岗位中的核心地位）